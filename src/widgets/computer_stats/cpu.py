import ttkbootstrap as ttkb
import psutil
from src import config


class CPUWidget(ttkb.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent

        # Style
        self.paragraph_font = ttkb.font.Font(family=config.FONT_FAMILY, size=config.PARAGRAPH_SIZE)
        self.annotation_font = ttkb.font.Font(family=config.FONT_FAMILY, size=config.ANNOTATION_SIZE)

        # Create elements
        self.title = ttkb.Label(self, text="CPU", font=self.paragraph_font)
        self.title.grid(row=0, column=0, padx=20)
        self.bar = None
        self.label = None

        self.update()

    def update(self):
        cpu = psutil.cpu_percent()

        self.bar = ttkb.Progressbar(self, value=cpu, style='Striped')
        self.label = ttkb.Label(self, text=f"{cpu}%", font=self.annotation_font)
        self.label.grid(row=2, column=0, padx=10, pady=0)
        self.bar.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        print(psutil.cpu_percent())
