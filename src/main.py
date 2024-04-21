import ttkbootstrap as ttkb
from src.widgets.computer_stats.container import Stats
from src.widgets.music_player.main import MusicPlayer
import config

class App(ttkb.Window):
    def __init__(self):
        super().__init__(themename=config.THEME_NAME)

        self.stats = Stats(master=self)
        self.music_player = MusicPlayer(master=self)

        self.after(1000, self.update)
        self.layout()

        # Configure Global Styles
        s = ttkb.Style()
        s.configure('TLabelframe.Label', font=(config.FONT_FAMILY, config.HEADING_SIZE))
        s.configure('TLabel', font=(config.FONT_FAMILY, config.PARAGRAPH_SIZE))

    def layout(self):
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.stats.grid(row=0, column=0, columnspan=5, padx=20, pady=20, sticky="new")
        self.music_player.grid(row=1, column=0, columnspan=10, padx=20, pady=20, sticky="new")

    def update(self):
        self.stats.update()
        self.after(1000, self.update)


window = App()
window.mainloop()
