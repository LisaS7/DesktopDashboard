import customtkinter as ctk
from src.widgets.computer_stats.widget import StatWidget

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 240


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.stat_frame = StatWidget(master=self)
        self.stat_frame.grid(row=0, column=0, columnspan=5, padx=20, pady=20, sticky="nsew")

        self.after(1000, self.stat_frame.update)


window = App()
window.mainloop()
