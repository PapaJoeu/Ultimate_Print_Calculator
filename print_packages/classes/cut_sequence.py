class CutSequence:
    def __init__(self, sheet_width, sheet_length, doc_width, doc_length, gutter_width, gutter_length):
        self.sheet_width = sheet_width
        self.sheet_length = sheet_length
        self.doc_width = doc_width
        self.doc_length = doc_length
        self.gutter_width = gutter_width
        self.gutter_length = gutter_length

    def calculate_sequence(self):
        # Calculations for Documents Across and Down
        self.docs_across = floor(self.sheet_width / (self.doc_width + self.gutter_width))
        self.docs_down = floor(self.sheet_length / (self.doc_length + self.gutter_length))
        self.total_docs = self.docs_across * self.docs_down
        self.total_gutter_width = (self.docs_across - 1) * self.gutter_width
        self.total_gutter_length = (self.docs_down - 1) * self.gutter_length
        self.imposed_space_width = (self.doc_width * self.docs_across) + self.total_gutter_width
        self.imposed_space_length = (self.doc_length * self.docs_down) + self.total_gutter_length
        self.top_bottom_lead = (self.sheet_length - self.imposed_space_length) / 2
        self.left_right_trim = (self.sheet_width - self.imposed_space_width) / 2

        cuts_and_slits = CutsAndSlits(self.sheet_width, self.sheet_length, self.doc_width, self.doc_length, self.gutter_width, self.gutter_length)
        cuts = cuts_and_slits.calculate_cuts()
        slits = cuts_and_slits.calculate_slits()

        return cuts, slits
    
        # Function to print margin and gutter cuts
    def print_margin_and_gutter_cuts():
        # print input variables
        print("Sheet W:", sheet_width)
        print("Sheet L:", sheet_length)
        print("Doc W:", doc_width)
        print("Doc L:", doc_length)
        print("Gutter W:", gutter_width)
        print("Gutter L:", gutter_length)
        print("Docs Across:", cut_sequence.docs_across)
        print("Docs Down:", cut_sequence.docs_down)
        print("Total Docs:", cut_sequence.total_docs)

        # Margin Cuts
        print("\nProgram Sequence:\n")
        print("1: {:.3f}".format(cuts[-1][1]))
        print("ROTATE")
        print("2: {:.3f} inches".format(slits[-1][1]))
        print("ROTATE")
        print("3: {:.3f} inches".format(cut_sequence.imposed_space_length))
        print("ROTATE")
        print("4: {:.3f} inches".format(cut_sequence.imposed_space_width))

        # Gutter Width Cuts
        gutter_pos_width = cut_sequence.imposed_space_width
        for i in range(cut_sequence.docs_across - 1):  # Iterate for each gutter between documents
            gutter_pos_width -= (cut_sequence.doc_width + cut_sequence.gutter_width)
            print(f"{5 + 2*i}: {gutter_pos_width:.3f} inches")

        # Rotate for Gutter Length Cuts
        print("ROTATE")

        # Gutter Length Cuts
        gutter_pos_length = cut_sequence.imposed_space_length
        for i in range(cut_sequence.docs_down - 1):  # Iterate for each gutter between documents
            gutter_pos_length -= (cut_sequence.doc_length + cut_sequence.gutter_length)
            seq_num = 5 + 2 * (cut_sequence.docs_across - 1) + 2 * i
            print(f"{seq_num}: {gutter_pos_length:.3f} inches")


    # Call the function to print the results
    print_margin_and_gutter_cuts()
