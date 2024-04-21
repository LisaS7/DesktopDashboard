import ttkbootstrap as ttkb
import psutil
from src import config


class CPUWidget(ttkb.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent

        self.paragraph_font = ttkb.font.Font(family=config.FONT_FAMILY, size=config.PARAGRAPH_SIZE)
        self.annotation_font = ttkb.font.Font(family=config.FONT_FAMILY, size=config.ANNOTATION_SIZE)

        self.title = ttkb.Label(self, text="CPU", font=self.paragraph_font)
        self.cpu_bar = None
        self.cpu_label = None
        self.update_cpu()

        self.layout()

    def layout(self):
        self.title.grid(row=0, column=0, padx=20, sticky="n")
        self.cpu_bar.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        ttkb.Label(self, text="").grid(row=2, column=0, padx=10, pady=0)

    def update_cpu(self):
        cpu = psutil.cpu_percent()

        self.cpu_bar = ttkb.Progressbar(self, value=cpu, style='Striped')
        self.cpu_label = ttkb.Label(self, text=f"{cpu}%", font=self.annotation_font)
        self.cpu_label.grid(row=2, column=0, padx=10, pady=0)
        self.cpu_bar.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        print(psutil.cpu_percent())
