import ttkbootstrap as ttkb
import psutil
from collections import namedtuple
from src.widgets.computer_stats.components import Title, Bar, Annotation

# todo: remove mock
# sbattery(percent=93, secsleft=16628, power_plugged=False)
BatteryMock = namedtuple("BatteryMock", ["percent", "secsleft", "power_plugged"])


class BatteryWidget(ttkb.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create elements
        self.title = Title(self, "Battery")
        self.bar = None
        self.label = None

        self.update()

    def update(self):
        battery = BatteryMock(90, 16628, False)  # psutil.sensors_battery()
        minutes_remaining = round(battery.secsleft / 60, 0)
        hours_remaining = round(minutes_remaining / 60, 1)

        if not battery or battery.power_plugged:
            pass  # todo: display power cable icon

        self.bar = Bar(self, value=battery.percent)
        self.label = Annotation(self, text="None")

        if hours_remaining >= 1:
            self.label = Annotation(self, text=f"{hours_remaining} hours left")
        else:
            self.label = Annotation(self, text=f"{minutes_remaining} minutes left")

