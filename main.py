# Task: Import the process and tui modules
# TODO: Your code here
import process
import tui
import os
# Task: Create an empty list named 'records'.

# This will be used to store the date read from the source data file.
# TODO: Your code here
records = []

def run():
    # Task: Use global keyword to reference the records variable in this function
    global records
    # Task: Call the function welcome of the module tui.
    # This will display our welcome message when the program is executed.
    # clearing a terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    tui.welcome() 


    while True:
        # Task: Using the appropriate function in the module tui, display a menu of options
        # for the different operations that can be performed on the data.
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        option = tui.main_menu()
        os.system('cls' if os.name == 'nt' else 'clear')
        if option == 1:
            print(tui.data_file_path())

        # Task: Check if the user selected the option for loading data.  If so, then do the following:
        # - Use the appropriate function in the tui module to indicate that data loading has started.
        # - Load the data (see below).
        # - Use the appropriate function in the tui module to indicate that data loading has completed.
        #
        # To load the data, do the following:
        # - Use the appropriate function in the tui module to retrieve a file path for the data file.
        # - Use the appropriate function in the process module to load the data using the specified file path.
        # - Set records to the result from calling the previous function.
        # TODO: Your code here

        # Task: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that data processing has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to indicate that data processing has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the tui module to display a menu of options for processing the data.
        # - Check which option has been selected and do the following for the selected option:
        #   - Use the appropriate function in the tui module indicate that the process has started.
        #   - Use the appropriate function in the process module to carry out the selected operation.
        #   - Use the appropriate function in the tui module to display the result.
        #   - Use the appropriate function the tui module to indicate the selection operation has completed.
        # TODO: Your code here

        # Task: Check if the user selected the option for visualising data.  If so, then do the following:
        # - Use the appropriate function in the tui module to indicate that data visualisation has started.
        # - Visualise the data (see below).
        # - Use the appropriate function in the tui module to indicate that data visualisation has completed.
        #
        # To visualise the data, do the following:
        # - Use the appropriate function in the tui module to display a menu of options for visualising the data.
        # - Check which option has been selected and do the following for the selected option:
        #   - Use the appropriate function in the tui module indicate that the process has started.
        #   - Add an appropriate function in the process module and use it to retrieve the data to be visualised.
        #   - Use the appropriate function in the visual module to generate the visualisation.
        #   - Use the appropriate function in the tui module to display the visualisation.
        #   - Use the appropriate function the tui module to indicate the selection operation has completed.
        # TODO: Your code here

        # Task: Check if the user selected the option for exiting.  If so, break out of the loop.
        # TODO: Your code here

        # Task: If the user selected an invalid option then use the appropriate function in the tui module to
        # display an error message
        # TODO: Your code here (remove pass below)
        pass


if __name__ == "__main__":
    run()
