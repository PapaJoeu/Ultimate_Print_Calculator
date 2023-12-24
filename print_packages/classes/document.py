class Document:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def __str__(self):
        return f"Document width: {self.width}, Document length: {self.length}"