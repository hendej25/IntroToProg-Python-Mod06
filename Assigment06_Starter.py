# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoFile.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# JHenderson,8.16.2022,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
FILENAME_STR = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dict = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection
task_str = ""  # Captures the user task data
priority_str = ""  # Captures the user priority data
status_str = ""  # Captures the status of a processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows.

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return:
            - (list) of dictionary rows
            - (string) indicating function status
        """
        #  (string) status:
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows.

        :param task: (string) with name of a task:
        :param priority: (string) with the task's priority:
        :param list_of_rows: (list) to which you want to add data:
        :return:
            - (list) of dictionary rows
            - (string) indicating function status
        """
        taskrow = {'Task': task, 'Priority': priority}
        list_of_rows.append(taskrow)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from a list of dictionary rows.

        :param task: (string) with name of a task:
        :param list_of_rows: (list) from which you want to remove data:
        :return:
            - (list) of dictionary rows
            - (string) indicating function status
        """
        taskfound = False
        for taskrow in list_of_rows:
            if taskrow['Task'].lower() == task.lower():
                list_of_rows.remove(taskrow)
                taskfound = True

        if taskfound:
            status = 'Success'
        else:
            status = 'Sorry, the task you entered is not one of the list items.'

        return list_of_rows, status

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a file.

        :param file_name: (string) with name of the file to which data should be written:
        :param list_of_rows: (list) containing data to be written out:
        :return:
            - (list) of dictionary rows
            - (string) indicating function status
        """
        file = open(file_name, 'w')
        for taskrow in list_of_rows:
            file.write(taskrow['Task'] + ',' + taskrow['Priority'] + '\n')

        file.close()

        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """ Shows the current tasks in the list of Dictionary rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current outstanding tasks are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Gets input from the user on a new task and its priority

        :return:
            - (string) task name
            - (string) task priority
        """
        task = input("Please enter a new task: ").title()
        priority = input("Priority (Low/Medium/High)?: ").title()
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Gets input from the user on a task to remove

        :return:
            - (string) task name
        """
        task = input('\nWhich task would you like to delete? ')
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, load data from ToDoFile.txt.
Processor.read_data_from_file(FILENAME_STR, table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 - Show current data
    IO.print_current_tasks_in_list(table_lst)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new task
        task_str, priority_str = IO.input_new_task_and_priority()
        table_lst, status_str = Processor.add_data_to_list(task_str, priority_str, table_lst)
        IO.input_press_to_continue(status_str)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing task
        task_str = IO.input_task_to_remove()
        table_lst, status_str = Processor.remove_data_from_list(task_str, table_lst)
        IO.input_press_to_continue(status_str)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        choice_str = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if choice_str.lower() == "y":
            table_lst, status_str = Processor.write_data_to_file(FILENAME_STR, table_lst)
            IO.input_press_to_continue(status_str)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif choice_str == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        choice_str = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if choice_str.lower() == 'y':
            table_lst, status_str = Processor.read_data_from_file(FILENAME_STR, table_lst)
            IO.input_press_to_continue(status_str)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif choice_str == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit

    else:  # if invalid choice, let the user know
        print("Please enter a valid choice [1-5].")
