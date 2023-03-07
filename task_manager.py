# importing libraries
import datetime as dt
from datetime import date
from datetime import datetime
# function to print out the task, uses two paramters, position of the line of text
# and element from line splited by split method
# funbction will use those paramters to print out number of task
# and organizes the text elements into the appropriate headings
def print_out_task(position, line):
    output =  f'_______________________{position}_________________________\n'
    output += '\n' 
    output += f'Assigned to: \t\t{line[0]}\n'               
    output += f'Task : \t\t\t{line[1]}\n'
    output += f'Date assigned: \t\t{line[2]}\n'
    output += f'Due date:  \t\t{line[3]}\n' 
    output += f'Task complete: \t\t{line[4]}\n'
    output += f'Task description: \t{line[5]}\n'
    output += '_________________________________________________\n'
    return output
# fuction to register new user
def reg_user(file):
    # variable to break the loop
    correct_username = False
    while True:
        # code to check if the username already exist
        while correct_username == False:
            # requesting the details from the user
            new_user_name = input('Enter a new username: ')
            # distionary to store usernames and passwords
            user_password = {}
            with open(file) as f:
                for line in f:
                    (username, password) = line.split(',')
                    user_password[username] = password
            # checking if the given username already exist
            if new_user_name in user_password:
                print(f'Username {new_user_name} already exist')
            else:
                # breaking the loop
                correct_username = True
        # requesting the password
        new_user_password = input('Enter your password: ')
        # requesting password repetition
        repeated_password = input('Please confirm your password:  ')
        # checking if the passwords match 
        if new_user_password == repeated_password:
            # opening the user.txt file and adding new user name and password
            with open(file, 'a') as f:
                f.write(new_user_name + ', ' + new_user_password + '\n')
            # breaking the loop
            break
        # printing out the message if the passwords do not match
        else:
            print('Passowrds do not match')
    return f'New user registration {new_user_name} successful'
# function to add new task
def add_task(date):
    # variable to store valid date format
    date_format = '%Y-%m-%d'
    while True:
        # opening the file, requesting the task details from the user
        # and adding those details to the list
        task_details = []
        with open('task.txt', 'a') as f:
            user_assigned_task = input('Enter name of user assigned to the task: ')
            task_title = input('Enter the task title: ')
            while True:
                # try except block to make sure that the given dat is in the correct format
                try:
                    due_date = input('Enter the task due date: (Year-month-day): ')
                    date_object = dt.datetime.strptime(due_date, date_format)
                    date_input = date_object.strftime(date_format)
                    break
                # wrong date format message
                except ValueError:
                    print('Wrong date format')                              
            description = input('Enter the task description: ')             
            task_details = ','.join([user_assigned_task, task_title, date, date_input, completion, description])+'\n'
            # adding task details to the file
            f.write(task_details)
        # option to add another task
        another_task = input('Would you like to enter another task? (yes/no)').lower()[0]
        if  another_task == 'n':
            break
# function to view all tasks
def view_all(data):
    for i, line in enumerate(data):
        # splitting the line of text using ',' separator
        line = line.split(',')
        # using print_out_function with i, line parameters
        # and printing out the resluts
        print(print_out_task(i, line))
# function to view the user tasks
def view_mine(data, name): 
    for i, line in enumerate(data):
        line = line.split(',')
        # checking if the name in the line of text with task details
        # match with logged user name
        if line[0] == name:
            print(print_out_task(i, line))
        # if the line does not contain current user name program will continue to another line
        else:
            continue
# fuction returns list with tasks indexes that belong to the user
def task_numbers(data, user_name):
    # list to store data
    tasks_numbers = []
    # loop to find tasks with logged user name
    for i, line in enumerate(data):
        line = line.split(',')
        if line[0] == user_name:
            tasks_numbers.append(i)
    return tasks_numbers

# login section
while (True):
    # dictionary to store data from the file
    user_password = {}
    with open('user.txt', 'r') as f:
        for line in f:
            (username, password) = line.split(', ')
            user_password[username] = password.replace('\n','')

    # requesting the user input
    user_name = input('Enter your user name: ')
    password = input('Enter your password: ')
    # checking if the given username already exist and if the password is correct
    if user_name in user_password and user_password[user_name] == password:
        # breaking the loop
        break
    else:
        print('Wrong username or password')
        
# while loop to run the program 
while True:
    # printing out the menu
    # requesting user to select the desired option from the menu  
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()
    completion = 'NO'
    # setting up today date
    today = str(date.today())
    # reading tasks from the file
    with open('task.txt', 'r') as f:
    # varibale storing all lines from the file
        data = f.readlines()
    # setting up number of tasks list and printing it out
    tasks_numbers = task_numbers(data, user_name)
    # this block of code is adding new user name and password to the user.txt file 
    if menu == 'r':
        reg_user('user.txt')
    # this block of code is adding new task to the task.txt file
    elif menu == 'a':
        add_task(today)
    # this block of code is printing out all tasks
    elif menu == 'va':
        view_all(data)
    # block of code to print out tasks to be performed by the loogged user 
    elif menu == 'vm':
        # using function to print out all task belong to the user
        view_mine(data,user_name)
        # printing out the task numbers belong to the user
        print(tasks_numbers)
        # block of code responsible of prinitng out task specified by the user and marking task as complete
        # and editing the specified task
        while True:
            # requesting input from the user
            user_selection = input(
                '''Please select one option:
        1. Show a specific task - r
        2. Quit - q
        ''')
            # if statement representing users choice (showing specific task)
            if user_selection == 'r':
                # loop to prevent user from the wrong  input
                while True:
                    # requesting input and specifing the correct choices
                    # user chooses specified task
                    selected_task = int(input(f'Enter the task number, tasks assigned to you {tasks_numbers}: '))
                    # wrong input condition
                    if selected_task not in tasks_numbers:
                        # wrong input information
                        print('Wrong task number. Use the number from the list. ')
                    # when input is correct breaking the loop
                    else: break
                # priniting out the task specified by the user
                print(print_out_task(selected_task, data[selected_task].split(',')))

                # Block of code responsible of smarking the task as completed
                # setting up varible which sotres the details of the task
                task = data[selected_task].split(',')
                # checking if task is not completed
                # if not program will print out option to mark it as completed
                if task[4] == 'NO':
                    mark_as_complete = input('Would you like to mark this task as complete?: (yes/no)').lower()[0]
                    # marking task as completed
                    if mark_as_complete == 'y':
                        task[4] = today
                        data[selected_task] = ','.join(task)
                    # option to edit task only if is not completed yet
                    elif task[4] == 'NO':
                        edit = input('Would you like to edit this task?: ').lower()[0]

                        # Block of code responsible of editing the task
                        # if user choose to edit task
                        if edit == 'y':
                            # new user assigned to the task
                            user_assigned_task = input('Enter name of user assigned to the task: ')
                            # new due date
                            due_date = input('Enter the task due date: ')                                             
                            # updating task details
                            task[0] = user_assigned_task
                            task[3] = due_date
                            # updating data varible
                            data[selected_task] = ','.join(task)
                        else:
                            continue
                    # updating the file
                    with open('task.txt', 'w') as f:
                        for line in data:
                            f.write(line)
            # breaking the loop
            elif user_selection == 'q':
                break
            # message about wrong input
            else:
                print('Wrong input.')
    # block of code responsible of generating the reports and store it into the file
    elif menu == 'gr':
        # setting up varibles 
        overdue_task_indexes = []
        user_report_data = []
        completed_tasks = 0
        uncompleted_tasks = 0
        overdue_tasks = 0
        # loop to go over the data in task file
        for i, line in enumerate(data):
            # i index of the task
            # line  stores details of task
            line = line.split(',')
            # if task uncompleted, the program will increase the number of uncopleted tasks
            if line[4] == 'NO':
                uncompleted_tasks += 1
                # converting due date and today date to date object
                due_date = datetime.strptime(line[3], '%Y-%m-%d').date()
                date_today = datetime.strptime(today,'%Y-%m-%d').date()
                # if due date is smaller than today date number of overdue tasks is incresed by 1
                # and index of overdue task is added to the overdue_task_indexes list
                if due_date < date.today():
                    overdue_task_indexes.append(i)
                    overdue_tasks += 1
            # if the task is completed, the number of completed tasks is increased by 1
            else:
                completed_tasks += 1
        # calculating ratios
        uncompleted_ratio = round((((len(data) - (len(data) - uncompleted_tasks)) / len(data)) * 100), 2) 
        overdue_ratio = round((((len(data)- (len(data) - overdue_tasks )) / len(data)) * 100), 2)
        # adding all calcultion to the list
        user_report_data = [completed_tasks, uncompleted_tasks, overdue_tasks, uncompleted_ratio, overdue_ratio]
        # variable that stores all the data in readble manner
        task_overview = f'-----Overall Statistics-----\n'
        task_overview += f'completed tasks: {user_report_data[0]}\n'
        task_overview += f'uncompleted tasks: {user_report_data[1]}\n'
        task_overview += f'overdue tasks: {user_report_data[2]}\n'
        task_overview += f'uncompleted ratio: {user_report_data[3]}\n'
        task_overview += f'overdue_ratio: {user_report_data[4]}\n'
        task_overview += f'---------------------------\n'
        # writing results to the file
        with open('task_overview.txt','w') as f:
            f.write(task_overview)
        with open('task_overview.txt','r') as f:
            f = f.readlines()
        # number of task that belong to the user
        user_tasks = len(tasks_numbers)
        # ratio calculations
        user_ratio = round((((len(data)- (len(data) - user_tasks )) / len(data)) * 100), 2)
        all_tasks_ratio = round((((len(data)- (len(data) - user_tasks )) / len(data)) * 100), 2)
        completed_user = 0
        # loops to calculate completed and overdue tasks
        for i in tasks_numbers:
            if 'YES' in data[i]:
                completed_user += 1
        overdue_user = 0
        for i in overdue_task_indexes:
            if user_name in data[i]:
                overdue_user += 1
        # if statements to prevent divindg by zero error
        # ratio calculations
        if user_tasks != 0:
            completed_ratio = round((((user_tasks - (user_tasks - completed_user )) / user_tasks) * 100), 2)
            overdue_user_ratio = round((((user_tasks - (user_tasks - overdue_user )) / user_tasks) * 100), 2)

        else:
            completed_ratio = 0
            overdue_user_ratio = 0
        to_do_ratio = 100 - completed_ratio
        titles = ['Total tasks: ', 'User tasks ratio: ','Completed task ratio: ', 'Uncompleted ratio: ', 'Overdue user ratio: ']
        user_report_data = [user_tasks, user_ratio, completed_ratio, to_do_ratio, overdue_user_ratio]

        # variable that stores all the data in readble manner
        user_task_overview = f'-----User Statistics-----\n'
        user_task_overview += f'Total tasks: {user_report_data[0]}\n'
        user_task_overview += f'User tasks ratio: {user_report_data[1]}\n'
        user_task_overview+= f'Completed task ratio: {user_report_data[2]}\n'
        user_task_overview += f'Uncompleted ratio: {user_report_data[3]}\n'
        user_task_overview += f'Overdue user ratio: {user_report_data[4]}\n'
        user_task_overview += f'---------------------------\n'
        # writing user statistics to the file
        with open('user_overview.txt', 'w') as f:
            f.write(user_task_overview)
    # block of code to print out the statistics
    elif menu == 'ds':
        print('Generate the report first, otherwise the data may be outdated.')
        # reading the data from the report files and using loop to print it out
        with open('task_overview.txt','r') as f:
            overal_stats = f.readlines()
        for line in overal_stats:
            print(line)
        with open('user_overview.txt', 'r')  as f:
            user_stats = f.readlines()
        for line in user_stats:
            print(line)

    # block of code to exit the program and print out 'Goodbye' message
    elif menu == 'e':
        print('Goodbye')
        # built in  exit function
        exit()
    # block of code to inform the user about wrong input
    else:
        print("You have made a wrong choice, Please Try again")




    

