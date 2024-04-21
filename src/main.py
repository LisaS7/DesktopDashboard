import ttkbootstrap as ttkb
from src.widgets.computer_stats.widget import StatWidget
import config


class App(ttkb.Window):
    def __init__(self):
        super().__init__(themename=config.THEME_NAME)
        self.stat_frame = None
        self.layout()
        self.add_widgets()
        
    def layout(self):
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def add_widgets(self):
        self.stat_frame = StatWidget(master=self)
        self.stat_frame.grid(row=0, column=0, columnspan=5, padx=20, pady=20, sticky="nsew")
        self.after(1000, self.stat_frame.update)


window = App()
window.mainloop()
