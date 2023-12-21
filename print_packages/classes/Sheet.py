class Sheet:
    def __init__(self, width=12, length=18):
        self.width = width
        self.length = length

    def __str__(self):
        return f"Sheet width: {self.width}, Sheet length: {self.length}"