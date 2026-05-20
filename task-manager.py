# Name: Reetisha Ojha


# Program Description:
    
# This program is a simple To-Do list that helps a user keep track of their tasks along with the due dates associated with each task. Each task has three pieces of information and the user can update its status. Each task will contain a text description, a due date in the form of a string, and a status that indicates whether the task is "Yet to start", "Pending", or "Completed". The program must be able to read an existing list of tasks from a text file, interpret the data correctly, and store the tasks into the correct Python data structures in order to be processed. 
# The program must allow the user to view all current tasks and their due dates, update the status along with the ability to add a new task by entering a description and due date. When any changes are made, the program must write all tasks back to an output text file to ensure the changes are saved. This program solves the problem of maintaining an organized list of tasks with specific deadlines.


# File that stores all tasks in the format: description | due date | status
FILENAME = "tasks.txt"

def load_tasks():
    # Loads all tasks from the text file and converts each line into a task dictionary.
    tasks = []
    f = open(FILENAME, "r")
    lines = f.readlines()
    f.close()
    
    for line in lines:
        # Removes extra whitespace.
        line = line.strip()
        
        if line != "":
            parts = line.split("|")
            
            # Handles missing due dates or statuses by assigning default values.
            if len(parts) == 3:
                desc = parts[0]
                due = parts[1]
                status = parts[2]
            elif len(parts) == 2:
                desc = parts[0]
                due = "No due date"
                status = parts[1]
            else:
                desc = line
                due = "No due date"
                status = "Pending"
            
            # Store task as dictionary for easier access in other functions.
            task = {"desc": desc, "due": due, "status": status}
            tasks.append(task)
                
    return tasks
        
            
def save_tasks(tasks):
    # Writes the current list of tasks back into the tasks.txt file in the correct format.
    f = open(FILENAME, "w")
    
    for task in tasks:
        line = task["desc"] + "|" + task["due"] + "|" + task["status"] + "\n"
        f.write(line)
    f.close()
    
def show_tasks(tasks):
    # Displays all tasks with numbering, status, descriptions, and due dates.
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            t = tasks[i]
            num = i + 1
            print(f"{num}. [{t['status']}] {t['desc']} (Due: {t['due']})")
        print()
        
def show_options():
    # Prints the main options for the user
    print("To-do List")
    print("-----------")
    print("1. View ongoing tasks")
    print("2. Add a new task")
    print("3. Change status of a task")
    print("4. Quit")
    
def add_task(tasks):
    # Adds a new task by asking the user for a description and due date.
    desc = input("Enter task and it's description: ").strip()
    
    if desc == "":
        print("Please enter a task.\n")
    else:
        due = input("Enter a due date: ").strip()
        # If the user leaves the due date blank, uses a default value.
        if due == "":
            due = "No due date"
            
        # New tasks always start with the status 'Yet to Start'.
        task = {"desc": desc, "due": due, "status": "Yet to Start"}
        tasks.append(task)
        
        # Immediately saves the updated task list to the file.
        save_tasks(tasks)
        print("Task added :D ""\n")
        
def change_status(tasks):
    # Allows the user to update the status of the selected task.
    
    # Prevents changing status if the list is empty.
    if len(tasks) == 0:
        print("No tasks to update.\n")
    else:
        show_tasks(tasks)
        num = input("Enter task number to change status: ")
        
        index = int(num) - 1
        
        if index >= 0 and index < len(tasks):
            current = tasks[index]["status"]
            print("Current status:", current)
            print("Choose new status:")
            print("1. Yet to Start")
            print("2. Pending")
            print("3. Completed")
            
            # Ensures user does not choose a task that doesn't exist.
            choice = input("Enter choice (1-3): ")
            
            if choice == "1":
                new_status = "Yet to Start"
            elif choice == "2":
                new_status = "Pending"
            elif choice == "3":
                new_status = "Completed"
            else:
                print("Invalid status choice.\n")
                
                return
            
            # Applies chosen status to the selected task and saves the changes.
            tasks[index]["status"] = new_status
            save_tasks(tasks)
            print("Status updated!\n")
        else:
            print("Invalid task number.\n")
            
def main():
    # Main program loop displays main options, processes the user's choices, and controls when the program exits
    
    # Loads existing tasks from the file at the start of the program.
    tasks = load_tasks()
    running = True
    while running:
        show_options()
        option = input("Choose an option: ")
        print()
        
        # Responding to user's choices
        if option == "1":
            show_tasks(tasks)
        elif option == "2":
            add_task(tasks)
        elif option == "3":
            change_status(tasks)
        elif option == "4":
            print("Goodbye! Have a nice day :p")
            running = False
        else:
            print("Invalid choice.\n")

main()
        