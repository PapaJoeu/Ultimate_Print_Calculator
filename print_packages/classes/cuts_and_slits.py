# cuts_and_slits.py
from print_packages.classes.Sheet import Sheet
from print_packages.classes.document import Document
from print_packages.classes.gutter import Gutter
from print_packages.classes.imposition import ImpositionMeasurements

# With the provided values:
# Sheet width: 12, Sheet length: 18
# Document width: 5, Document length: 7
# Gutter width: 0.125, Gutter length: 0.125
# Imposition Measurements:
# Docs Across: 2
# Docs Down: 2
# Total Pages Per Sheet: 4
# Lead Trim: 0.875
# Side Trim: 1.875
# Imposed Width: 10.25
# Imposed Length: 14.25
# The output of the CutsAndSlits should be:
# Cuts: [1.938, 8.938, 9.063, 16.063, 16.188], Slits: [0.938, 5.938, 6.063, 11.063]

class CutsAndSlits:
    def __init__(self, sheet: Sheet, document: Document, gutter: Gutter, imposition: ImpositionMeasurements):
        self.sheet = sheet
        self.document = document
        self.gutter = gutter
        self.imposition = imposition

    def calculate_cuts(self):
        cuts = []
        for i in range(self.imposition.docs_down):
            cut = self.imposition.side_trim + i * (self.document.length + self.gutter.length)
            cuts.extend([cut, cut + self.gutter.length])
        cuts.append(self.imposition.side_trim + self.imposition.docs_down * self.document.length + self.imposition.docs_down * self.gutter.length)
        return cuts
    
    def calculate_slits(self):
        slits = []
        for i in range(self.imposition.docs_across):
            slit = self.imposition.side_trim + i * (self.document.width + self.gutter.width)
            slits.extend([slit, slit + self.gutter.width])
        slits.append(self.imposition.side_trim + self.imposition.docs_across * self.document.width + self.imposition.docs_across * self.gutter.width)
        return slits

    def __str__(self):
        cuts = self.calculate_cuts()
        slits = self.calculate_slits()
        return f"Cuts: {cuts}, Slits: {slits}"