import customtkinter as ctk
import psutil
from collections import namedtuple
from src import config

# sbattery(percent=93, secsleft=16628, power_plugged=False)
BatteryMock = namedtuple("BatteryMock", ["percent", "secsleft", "power_plugged"])


class BatteryWidget(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.paragraph_font = ctk.CTkFont(family=config.FONT_FAMILY, size=config.PARAGRAPH_SIZE)
        self.annotation_font = ctk.CTkFont(family=config.FONT_FAMILY, size=config.ANNOTATION_SIZE)
        self.title = ctk.CTkLabel(self, text="Battery", font=self.paragraph_font)
        # self.battery = BatteryMock(93, 16628, False)  #psutil.sensors_battery()

        self.battery_bar = ctk.CTkProgressBar(self)
        self.update_battery()

        self.time_remaining_label = ctk.CTkLabel(self, text="None", font=self.annotation_font)
        self.update_time_remaining()

        # Layout
        self.title.grid(row=0, column=0, padx=20)
        self.battery_bar.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        self.time_remaining_label.grid(row=2, column=0, padx=10, pady=0, sticky="n")

    def update_battery(self):
        battery = BatteryMock(23, 16628, False)  # psutil.sensors_battery()
        battery_decimal = battery.percent / 100
        if battery:
            self.battery_bar.set(battery_decimal)
        else:
            pass
        # display power cable icon

    def update_time_remaining(self):
        battery = BatteryMock(23, 16628, False)  # psutil.sensors_battery()
        minutes_remaining = round(battery.secsleft / 60, 0)
        hours_remaining = round(minutes_remaining / 60, 1)
        if hours_remaining >= 1:
            self.time_remaining_label.configure(text=f"{hours_remaining} hours left")
        else:
            self.time_remaining_label.configure(text=f"{minutes_remaining} minutes left")
