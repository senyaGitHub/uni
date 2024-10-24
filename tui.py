
def welcome(width=100):
    """
    Task: Display a welcome message.

    The title 'Titanic Records System' should be displayed.
    A line of dash characters (i.e. -) should be displayed above and below the title.
    The number of dashes should be equal to the width parameter.
    The title should appear in the center horizontally.
    For example, if width is 50, the following should be produced:

    --------------------------------------------------
                  Titanic Records System
    --------------------------------------------------

    :return: Does not return anything.
    """

    # Calculate the number of dashes
    dashes = '-' * width

    # Print the dashes above
    print(dashes)

    # Calculate spaces for centering the title
    spaces = ((width - len("Titanic Records System")) // 2)
    print(" " * int(spaces) + "Titanic Records System")

    # Print the dashes below
    print(dashes)



def main_menu():
    while True:
        try:
            option = int(input(''' 
    Main Menu:
      [1] Load Data
      [2] Process Data
      [3] Visualise Data
      [4] Exit
    Select option:
    '''))
            if option in range(1,5):
                return option
            else:
                print("Choose an option between 1 and 4. ")
        except Exception as e:
            error("please enter a number.")
            pass


def data_file_path():
    default_path = "data/titanic.csv"
    user_input = input("Please enter the file path for the data file (e.g., data/titanic.csv): ")

    if not user_input.endswith('.csv'):
        error("The file path must end with '.csv'. Returning the default path.")
        return default_path

    return user_input


def progress(operation, percent):
    """
    Task: Display a message to indicate the status of an operation.

    The function should display a message in the following format:
    '--- {operation}: {status} ---'
    Where:
     {operation} is the value of the operation parameter passed to this function in uppercase.
     {status} is "STARTED" if the value of the percent parameter is 0
              is "COMPLETED" if the value of the percent parameter is 100
              is "IN PROGRESS (X%)" where X is the value of percent parameter and is between 0 and 100

    Additionally:
        - a blank line should be displayed before the message where the status is STARTED i.e. percent is 0.
        - a blank line should be displayed after the message where the status is COMPLETED i.e. percent is 100.

    For  example, if the operation is "Data Loading" and the percent is 0, the following would be displayed:

    --- DATA LOADING: STARTED ---

    :param operation: A string indicating the operation being started
    :param percent: An integer between 0 - 100 indicating the progress percentage
    :return: Does not return anything
    """

    if percent == 0:
        print()
        print(f'~~~ {operation.upper()}: STARTED ~~~')
    elif percent == 100:
        print(f'~~~ {operation.upper()}: COMPLETED ~~~')
        print()
    else:
        print(f'~~~ {operation.upper()}: IN PROGRESS ({percent}%) ~~~')


def error(error_msg):
    """
    Task: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter passed to this function

    :param error_msg: A string containing an error message
    :return: Does not return anything
    """
    # TODO: Your code here (remove pass below)
    print(f"Error! {error_msg}")


def process_menu():
    """
    Task: Display a menu of options for how the data should be processed. Read in and return the user's response.

    A menu should be displayed that contains the following options:
        'Extract Passenger Names',
        'Count Survivors',
        'Count Passengers Per Gender',
        'Count Passengers Per Age Group',
        'Return to main menu'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Extract Passenger Names', 2 for 'Count Survivors' and so on.

    If the user enters an invalid option then:
     - a suitable error message should be displayed
     - the user should be prompted to select again until a valid option is selected.

    :return: An integer corresponding to a valid option
    """
    # TODO: Your code here (remove pass below)
    while True:
        try:
            option = int(input(''' 
      [1] Extract Passenger Names
      [2] Count Survivors
      [3] Count Passengers Per Gender
      [4] Count Passengers Per Age Group
    Select option:
      [5] Return to main menu
    '''))
            if option in range(1,6):
                return option
            else:
                print("Choose an option between 1 and 5. ")
        except Exception as e:
            error("please enter a number.")
            pass


def display_passenger_names(passenger_names):
    """
    Task: Display the name of each passenger in a list of passenger names.

    The passenger_names parameter should contain a list of passenger names (strings).
    If passenger_names is None or an empty list then a suitable error message should be displayed.
    Otherwise, each name (string) in the list should be displayed.

    Hint: You can use the len() function to determine how many items are in the list

    :param passenger_names: A list of passenger names
    :return: None
    """
    # TODO: You code here (remove pass below)
    pass


def display_survivor_count(survivor_count):
    """
    Task: Display the number of survivors.

    The function should display the value of the survivor_count parameter.

    :param survivor_count: An integer corresponding to the number of survivors
    :return: None
    """
    # TODO: Your code here (remove pass below)
    pass


def display_sex_counts(sex_counts):
    """
    Task: Display the number of passengers of each sex.

    The sex_counts parameter contains two values:
        - the number of males
        - the number of females.
    The function should display each of the values with a suitable message.

    :param sex_counts: A sequence containing the number males and females.
    :return: None
    """
    # TODO: Your code here (remove pass below)
    pass


def display_age_group_counts(age_group_counts):
    """
    Task: Display the number of passengers in each age group.

    The age_group_counts parameter contains three values:
     - the number of children
     - the number of adults
     - the number of elderly
    The function should display each of the values with a suitable message.

    :param age_group_counts: A sequence containing the number children, adults, and elderly.
    :return: None
    """
    # TODO: Your code here (remove pass below)
    pass


def visual_menu():
    """
    Task: Display a menu of options for how the data should be visualised. Read in and return the user's response.

    A menu should be displayed that contains the following options:
        'Passenger Class Horizontal Bar Graph',
        'Return to main menu'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Passenger Class Bar Graph' and 2 for 'Return to main menu'.

    If the user enters an invalid option then:
     - a suitable error message should be displayed
     - the user should be prompted to select again until a valid option is selected.

    :return: An integer corresponding to a valid option
    """
    # TODO: Your code here (remove pass below)
    pass


def display_visual(visual):
    """
    Display the visual.

    The function should display the visual.

    :param visual: A string containing appropriate ASCII art.
    :return: None
    """
    # TODO: Your code here (remove pass below)
    pass
