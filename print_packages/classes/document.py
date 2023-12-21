class Document:

    def __init__(self, width=5, length=7):
        self.width = width
        self.length = length

    def __str__(self):
        return f"Document width: {self.width}, Document length: {self.length}"