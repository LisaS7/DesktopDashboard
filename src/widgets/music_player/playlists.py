import ttkbootstrap as ttkb
from .tracks import Tracks

class Playlists(ttkb.Treeview):
    def __init__(self, master, data):
        super().__init__(master, columns="col1")
        self.master = master
        self.grid(row=0, column=0, padx=20)
        self.current_playlist = None
        self.tracks = None
        self.playlists = data
        self.insert_playlists()
        self.bind('<<TreeviewSelect>>', self.playlist_selected)

    def insert_playlists(self):
        for k, v in self.playlists.items():
            self.insert('', ttkb.END, values=[k], iid=v)

    def playlist_selected(self, event):
        for item in self.selection():
            self.current_playlist = item
            self.get_tracks()

    def get_tracks(self):
        result = self.master.sp.playlist(self.current_playlist)
        self.tracks = Tracks(self, result['tracks']['items'])
