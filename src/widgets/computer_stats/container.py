import ttkbootstrap as ttkb
from .battery import BatteryWidget
from .cpu import CPUWidget
from src import config


class StatWidget(ttkb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.heading_font = ttkb.font.Font(family=config.FONT_FAMILY, size=config.HEADING_SIZE)

        self.label = ttkb.Label(self, text="Computer Stats", font=self.heading_font)
        self.label.grid(row=0, column=0, padx=20)

        self.battery_widget = BatteryWidget(self)
        self.battery_widget.grid(row=1, column=0, padx=20)

        self.CPU_widget = CPUWidget(self)
        self.CPU_widget.grid(row=1, column=1, padx=20)

    def update(self):
        self.battery_widget.update()
        self.CPU_widget.update()
