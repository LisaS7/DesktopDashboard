import customtkinter as ctk
from .battery import BatteryWidget
from src import config

class StatWidget(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.heading_font = ctk.CTkFont(family=config.FONT_FAMILY, size=config.HEADING_SIZE)

        self.label = ctk.CTkLabel(self, text="Computer Stat Frame", font=self.heading_font)
        self.label.grid(row=0, column=0, padx=20)

        self.battery_widget = BatteryWidget(self)
        self.battery_widget.grid(row=1, column=0, padx=20)

    def update(self):
        self.battery_widget.update_battery()


