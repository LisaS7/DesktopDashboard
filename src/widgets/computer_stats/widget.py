import customtkinter as ctk
from .battery import BatteryWidget


class StatWidget(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label = ctk.CTkLabel(self, text="Computer Stat Frame")
        self.label.grid(row=0, column=0, padx=20)

        self.battery_widget = BatteryWidget(self)
        self.battery_widget.grid(row=1, column=0, padx=20)

    def update(self):
        self.battery_widget.update_battery()


