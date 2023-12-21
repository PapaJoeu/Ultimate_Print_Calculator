from print_packages.classes.Sheet import Sheet
from print_packages.classes.document import Document
from print_packages.classes.gutter import Gutter
from print_packages.classes.imposition import ImpositionMeasurements
from print_packages.classes.cuts_and_slits import CutsAndSlits

TEST_MODE = True  # Set this to False to use the provided values

DEFAULT_PAPER_WIDTH = 12
DEFAULT_PAPER_LENGTH = 18

DEFAULT_DOCUMENT_WIDTH = 5
DEFAULT_DOCUMENT_LENGTH = 7

DEFAULT_GUTTER_WIDTH = 0.125
DEFAULT_GUTTER_LENGTH = 0.125

# If TEST_MODE is True, the default values will be used. 
# If TEST_MODE is False, the provided values will be used.
if TEST_MODE:
    sheet = Sheet(DEFAULT_PAPER_WIDTH, DEFAULT_PAPER_LENGTH)
    doc = Document(DEFAULT_DOCUMENT_WIDTH, DEFAULT_DOCUMENT_LENGTH)
    gutter = Gutter(DEFAULT_GUTTER_WIDTH, DEFAULT_GUTTER_LENGTH)
else:
    # Replace these with the values provided by the user
    user_paper_width = 13
    user_paper_length = 19
    user_document_width = 8.5
    user_document_length = 11
    user_gutter_width = 0.25
    user_gutter_length = 0.25

    sheet = Sheet(user_paper_width, user_paper_length)
    doc = Document(user_document_width, user_document_length)
    gutter = Gutter(user_gutter_width, user_gutter_length)

imposition = ImpositionMeasurements(sheet, doc, gutter)
cuts_and_slits = CutsAndSlits(sheet, doc, gutter, imposition)

print(sheet)
print(doc)
print(gutter)
print(imposition)
print(cuts_and_slits)
