import json
from print_packages.classes.Sheet import Sheet
from print_packages.classes.document import Document
from print_packages.classes.gutter import Gutter

class UserSettingsManager:
    settings_file = 'settings.json'

    @classmethod
    def load_user_settings(cls):
        try:
            with open(cls.settings_file, 'r') as f:
                settings = json.load(f)
        except FileNotFoundError:
            settings = {
                'default_sheet_width': 12,
                'default_sheet_length': 18,
                'default_document_width': 5,
                'default_document_length': 7,
                'default_gutter_width': 0.125,
                'default_gutter_length': 0.125
            }
        return settings

    @classmethod
    def save_user_settings(cls, settings):
        with open(cls.settings_file, 'w') as f:
            json.dump(settings, f)

    @classmethod
    def update_user_settings(cls):
        settings = cls.load_settings()
        settings['default_sheet_width'] = float(input("Enter new default Sheet Width: ") or settings['default_sheet_width'])
        settings['default_sheet_length'] = float(input("Enter new default Sheet Length: ") or settings['default_sheet_length'])
        settings['default_document_width'] = float(input("Enter new default Document Width: ") or settings['default_document_width'])
        settings['default_document_length'] = float(input("Enter new default Document Length: ") or settings['default_document_length'])
        settings['default_gutter_width'] = float(input("Enter new default Gutter Width: ") or settings['default_gutter_width'])
        settings['default_gutter_length'] = float(input("Enter new default Gutter Length: ") or settings['default_gutter_length'])
        cls.save_user_settings(settings)
        print("Settings updated with the following values:")
        print(f"Default Sheet: {settings['default_sheet_width']} x {settings['default_sheet_length']}")
        print(f"Default Document: {settings['default_document_width']} x {settings['default_document_length']}")
        print(f"Default Gutter: {settings['default_gutter_width']} x {settings['default_gutter_length']}")

class UserInputCollector:
    @classmethod
    def collect_user_input(cls):
        settings = UserSettingsManager.load_user_settings()

        sheet_width = float(input(f"Enter Sheet Width (default {settings['default_sheet_width']}): ") or settings['default_sheet_width'])
        sheet_length = float(input(f"Enter Sheet Length (default {settings['default_sheet_length']}): ") or settings['default_sheet_length'])
        sheet = Sheet(sheet_width, sheet_length)

        document_width = float(input(f"Enter Document Width (default {settings['default_document_width']}): ") or settings['default_document_width'])
        document_length = float(input(f"Enter Document Length (default {settings['default_document_length']}): ") or settings['default_document_length'])
        document = Document(document_width, document_length)

        gutter_width = float(input(f"Enter Gutter Width (default {settings['default_gutter_width']}): ") or settings['default_gutter_width'])
        gutter_length = float(input(f"Enter Gutter Length (default {settings['default_gutter_length']}): ") or settings['default_gutter_length'])
        gutter = Gutter(gutter_width, gutter_length)

        return sheet, document, gutter

class UserInteractionManager:
    @classmethod
    def welcome_user_and_get_input(cls):
        print("Welcome to the Imposition Calculator!")
        while True:
            print("1. Change default settings")
            print("2. Enter new measurements")
            print("3. Exit")
            selection = int(input("Please select an option: "))
            if selection == 1:
                UserSettingsManager.update_user_settings()
            elif selection == 2:
                return UserInputCollector.collect_user_input()
            elif selection == 3:
                exit()
            else:
                print("Invalid selection. Please try again.")