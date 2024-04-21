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

        self.sp = None
        self.spotify_auth()

        self.get_playlists()
        self.tracks = None

    def spotify_auth(self):
        dotenv.load_dotenv()
        client_id = os.environ['SPOTIFY_CLIENT_ID']
        client_secret = os.environ['SPOTIFY_SECRET']
        redirect_uri = 'http://localhost/'

        auth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
        sp = spotipy.Spotify(auth_manager=auth)

        self.sp = sp

    def get_playlists(self):
        result = self.sp.current_user_playlists()
        self.playlists = Playlists(self, result)

    def get_tracks(self):
        result = self.sp.playlist(self.playlists.current_playlist)
        self.tracks = Tracks(self, result['tracks']['items'])

