import ttkbootstrap as ttkb
import psutil
from src.widgets.computer_stats.components import Title, Bar, Annotation


class RAMWidget(ttkb.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create elements
        self.title = Title(self, "RAM")
        self.bar = None
        self.label = None

        self.update()

    def update(self):
        ram_used = psutil.virtual_memory().percent
        ram_total = int(round(psutil.virtual_memory().total / 2**30, 0))
        self.bar = Bar(self, value=ram_used)
        self.label = Annotation(self, text=f"{ram_used}% of {ram_total}GB")
