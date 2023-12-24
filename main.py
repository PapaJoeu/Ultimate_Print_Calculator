from print_packages.classes.imposition import ImpositionMeasurements
from print_packages.classes.user_input import UserInteractionManager

def run_imposition_calculator():
    sheet, document, gutter = UserInteractionManager.welcome_user_and_get_input()
    imposition = ImpositionMeasurements(sheet, document, gutter)
    print(imposition)


if __name__ == "__main__":
    run_imposition_calculator()