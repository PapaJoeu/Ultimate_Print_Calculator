class Gutter:

    def __init__(self, width=0.125, length=0.125):
        self.width = width
        self.length = length

    def __str__(self):
        return f"Gutter width: {self.width}, Gutter length: {self.length}"