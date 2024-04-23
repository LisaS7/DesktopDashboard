import ttkbootstrap as ttkb
import dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from src import config
from .playlists import Playlists
from .tracks import Tracks

dotenv.load_dotenv()
client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_SECRET']
redirect_uri = 'http://localhost/'


class MusicPlayer(ttkb.Labelframe):

    def __init__(self, master):
        super().__init__(master, text="Music")
        self.master = master

        self.client = None
        self.device = None
        self.spotify_auth()
        self.set_device()

        self.playlists = None
        self.get_playlists()
        self.tracks = None
        self.is_playing = False

        control_frame = ttkb.Frame(self)
        control_frame.grid(row=0, column=2)
        self.play_pause_button = ttkb.Button(control_frame, text='⏵', command=self.play_pause)
        self.play_pause_button.grid(row=0, column=0)

    def spotify_auth(self):
        auth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,
                            scope=config.spotipy_scope)
        sp = spotipy.Spotify(auth_manager=auth)
        self.client = sp

    def set_device(self):
        self.device = self.client.devices()['devices'][0]

    def get_playlists(self):
        result = self.client.current_user_playlists()
        self.playlists = Playlists(self, result)

    def get_tracks(self):
        result = self.client.playlist(self.playlists.current_playlist)
        self.tracks = Tracks(self, result['tracks']['items'])

    def play(self, track):
        track = self.client.track(track)
        self.client.start_playback(self.device['id'], uris=[track['uri']])
        self.is_playing = True
        self.play_pause_button.configure(text='⏸')

    def play_pause(self):
        if self.is_playing:
            self.client.pause_playback()
            self.play_pause_button.configure(text='⏵')
        else:
            self.client.start_playback()
            self.play_pause_button.configure(text='⏸')
        self.is_playing = not self.is_playing
