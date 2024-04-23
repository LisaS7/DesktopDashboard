import ttkbootstrap as ttkb


class Tracks(ttkb.Treeview):
    columns = ('name', 'artist', 'album')

    def __init__(self, master, data):
        super().__init__(master, columns=self.columns, show='headings')
        self.master = master
        self.grid(row=0, column=1, padx=10, pady=10, sticky="nes")
        self.heading('name', text='Name')
        self.heading('artist', text='Artist')
        self.heading('album', text='Album')
        self.parse_result(data)
        self.bind('<<TreeviewSelect>>', self.play_track)

    def parse_result(self, data):
        for track in data:
            name = track['track']['name']
            artist = track['track']['artists'][0]['name']
            album = track['track']['album']['name']
            id = track['track']['id']
            self.insert('', ttkb.END, values=(name, artist, album), iid=id)

    def play_track(self, event):
        for item in self.selection():
            self.master.play(item)



