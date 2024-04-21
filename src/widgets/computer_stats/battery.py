import ttkbootstrap as ttkb
import psutil
from collections import namedtuple
from src import config

# sbattery(percent=93, secsleft=16628, power_plugged=False)
BatteryMock = namedtuple("BatteryMock", ["percent", "secsleft", "power_plugged"])


class BatteryWidget(ttkb.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent

        # Style
        self.paragraph_font = ttkb.font.Font(family=config.FONT_FAMILY, size=config.PARAGRAPH_SIZE)
        self.annotation_font = ttkb.font.Font(family=config.FONT_FAMILY, size=config.ANNOTATION_SIZE)

        # Create elements
        self.title = ttkb.Label(self, text="Battery", font=self.paragraph_font)
        self.battery_bar = None
        self.time_remaining_label = ttkb.Label(self, text="None", font=self.annotation_font)

        self.layout()

    def layout(self):
        self.title.grid(row=0, column=0, padx=20)

        self.update_battery()
        self.battery_bar.grid(row=1, column=0, padx=20, pady=10, sticky="n")

        self.update_time_remaining()
        self.time_remaining_label.grid(row=2, column=0, padx=10, pady=0, sticky="n")

    def update_battery(self):
        battery = BatteryMock(90, 16628, False)  # psutil.sensors_battery()
        if battery:
            self.battery_bar = ttkb.Progressbar(self, value=battery.percent)
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
