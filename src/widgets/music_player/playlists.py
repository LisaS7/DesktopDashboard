import ttkbootstrap as ttkb
from .tracks import Tracks


class Playlists(ttkb.Treeview):
    def __init__(self, master, data):
        super().__init__(master, columns="heading", show='headings')
        self.heading('heading', text="Playlists")
        self.master = master
        self.grid(row=0, column=0, padx=10, pady=10, sticky="nes")
        self.current_playlist = None
        self.parse_result(data)
        self.bind('<<TreeviewSelect>>', self.playlist_selected)

    def parse_result(self, data):
        for playlist in data['items']:
            self.insert('', ttkb.END, values=playlist['name'], iid=playlist['id'])

    def playlist_selected(self, event):
        for item in self.selection():
            self.current_playlist = item
            self.master.get_tracks()


