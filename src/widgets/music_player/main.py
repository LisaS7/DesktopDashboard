import ttkbootstrap as ttkb
import dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from .playlists import Playlists
from .tracks import Tracks

class MusicPlayer(ttkb.Labelframe):
    def __init__(self, master):
        super().__init__(master, text="Music")
        self.master = master

        self.client = None
        self.device = None
        self.spotify_auth()

        self.get_playlists()
        self.tracks = None
        self.playing = False

        control_frame = ttkb.Frame(self)
        control_frame.grid(row=0, column=2)
        play_pause_button = ttkb.Button(control_frame, text='test', command=self.play_pause)
        play_pause_button.grid(row=0, column=0)

        # self.controls = Controls(self, device=self.device, client=self.client)

    def spotify_auth(self):
        dotenv.load_dotenv()
        client_id = os.environ['SPOTIFY_CLIENT_ID']
        client_secret = os.environ['SPOTIFY_SECRET']
        redirect_uri = 'http://localhost/'

        scope = [
            "user-read-email",
            "user-read-private",
            "user-modify-playback-state",
            "user-read-playback-state",
            "user-read-currently-playing",
            "user-read-recently-played",
            "user-read-playback-position",
            "user-top-read",
        ]

        auth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
        sp = spotipy.Spotify(auth_manager=auth)

        self.device = sp.devices()['devices'][0]

        self.client = sp

    def get_playlists(self):
        result = self.client.current_user_playlists()
        self.playlists = Playlists(self, result)

    def get_tracks(self):
        result = self.client.playlist(self.playlists.current_playlist)
        self.tracks = Tracks(self, result['tracks']['items'])

    def play(self, track):
        track = self.client.track(track)
        self.client.start_playback(self.device['id'], uris=[track['uri']])
        self.playing = True

    def play_pause(self):
        print(self.playing)
        if self.playing:
            self.client.pause_playback()
        else:
            self.client.start_playback()
        self.playing = not self.playing


