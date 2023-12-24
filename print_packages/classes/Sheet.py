class Sheet:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def __str__(self):
        return f"Sheet width: {self.width}, Sheet length: {self.length}"