import ttkbootstrap as ttkb
from src import config


class Title(ttkb.Label):
    def __init__(self, parent, text):
        super().__init__(parent, text=text)
        self.grid(row=0, column=0, padx=20)


class Bar(ttkb.Progressbar):
    def __init__(self, parent, value):
        super().__init__(parent, value=value, style='Striped')
        self.grid(row=1, column=0, padx=20, pady=10, sticky="n")


class Annotation(ttkb.Label):
    def __init__(self, parent, text):
        self.font = ttkb.font.Font(family=config.FONT_FAMILY, size=config.ANNOTATION_SIZE)
        super().__init__(parent, text=text, font=self.font)
        self.grid(row=2, column=0, padx=10, pady=0)
