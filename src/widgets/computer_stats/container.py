import ttkbootstrap as ttkb
from .battery import BatteryWidget
from .cpu import CPUWidget
from .ram import RAMWidget


class StatWidget(ttkb.Labelframe):
    def __init__(self, master):
        super().__init__(master, text="Stats")
        self.master = master

        self.battery_widget = BatteryWidget(self)
        self.battery_widget.grid(row=1, column=0, padx=20)

        self.CPU_widget = CPUWidget(self)
        self.CPU_widget.grid(row=1, column=1, padx=20)

        self.RAM_widget = RAMWidget(self)
        self.RAM_widget.grid(row=1, column=2, padx=20)

    def update(self):
        self.battery_widget.update()
        self.CPU_widget.update()
        self.RAM_widget.update()
