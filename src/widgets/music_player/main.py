import ttkbootstrap as ttkb
import dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from .playlists import Playlists


class MusicPlayer(ttkb.Labelframe):
    def __init__(self, master):
        super().__init__(master, text="Music")
        self.master = master

        self.sp = None
        self.spotify_auth()

        playlist_result = self.get_playlists()
        self.playlists = Playlists(self, playlist_result)

    def spotify_auth(self):
        dotenv.load_dotenv()
        client_id = os.environ['SPOTIFY_CLIENT_ID']
        client_secret = os.environ['SPOTIFY_SECRET']
        redirect_uri = 'http://localhost/'

        auth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
        sp = spotipy.Spotify(auth_manager=auth)

        self.sp = sp

    def get_playlists(self):
        playlists = self.sp.current_user_playlists()
        playlist_dict = {}
        for playlist in playlists['items']:
            playlist_dict[playlist['name']] = playlist['id']
        return playlist_dict
