# imposition.py   

import math
from print_packages.classes.document import Document
from print_packages.classes.Sheet import Sheet
from print_packages.classes.gutter import Gutter

class ImpositionMeasurements:
    def __init__(self, sheet, document, gutter):
        self.sheet = sheet
        self.document = document
        self.gutter = gutter

        # calculate the max number of rows and columns that can fit on a sheet based on the sheet and document dimensions and gutters
        self.docs_across = math.floor((self.sheet.width - self.gutter.width) / (self.document.width + self.gutter.width))
        self.docs_down = math.floor((self.sheet.length - self.gutter.length) / (self.document.length + self.gutter.length))
        self.total_pages_per_sheet = self.docs_across * self.docs_down
        self.lead_trim = (self.sheet.width - ((self.document.width + self.gutter.width) * self.docs_across)) / 2
        self.side_trim = (self.sheet.length - ((self.document.length + self.gutter.length) * self.docs_down)) / 2
        self.imposed_width = self.sheet.width - (self.lead_trim * 2)
        self.imposed_length = self.sheet.length - (self.side_trim * 2)

    def __str__(self):
        return f"Imposition Measurements:\nDocs Across: {self.docs_across}\nDocs Down: {self.docs_down}\nTotal Pages Per Sheet: {self.total_pages_per_sheet}\nLead Trim: {self.lead_trim}\nSide Trim: {self.side_trim}\nImposed Width: {self.imposed_width}\nImposed Length: {self.imposed_length}"