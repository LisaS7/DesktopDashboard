import ttkbootstrap as ttkb
import psutil
from src.widgets.computer_stats.components import Title, Bar, Annotation


class CPUWidget(ttkb.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create elements
        self.title = Title(self, "CPU")
        self.bar = None
        self.label = None

        self.update()

    def update(self):
        cpu = psutil.cpu_percent()
        self.bar = Bar(self, value=cpu)
        self.label = Annotation(self, text=f"{cpu}%")
