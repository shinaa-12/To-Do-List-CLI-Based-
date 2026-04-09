import json
import os

# to manage the tasks even if the machine is rebooted, we will save the tasks in a json file. You can change the path as needed..
file_path = './tasks.json' 

#colors for the Command Line
class Colors:
    RESET = "\033[0m"
    WHITE = "\033[97m"
    TITLE = "\033[95m"
    QUESTION = "\033[96m"
    INFO = "\033[94m"
    YELLOW = "\033[93m"
    SUCCESS = "\033[92m"
    ERROR = "\033[91m"

#Function to color the text in the terminal
def color_text(text, color):
    return f"{color}{text}{Colors.RESET}"

#Clears the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#loads the task from file to program
def load_tasks(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []

#saves back to file
def save_tasks(path, tasks):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=2)

#display message
def display_menu(toast_message=""):
    if toast_message:
        print(color_text(toast_message, Colors.WHITE))
    print(color_text("\nTo-Do Menu", Colors.TITLE))
    print(color_text("1. Add Task", Colors.SUCCESS))
    print(color_text("2. View Tasks", Colors.INFO))
    print(color_text("3. Remove Task", Colors.ERROR))
    print(color_text("4. Delete All Tasks", Colors.ERROR))
    print(color_text("5. Exit", Colors.YELLOW))

#adds task to the running list
def add_task(tasks, path):
    task = input(color_text("Enter task: ", Colors.QUESTION)).strip()
    if not task:
        return "Task cannot be empty"
    tasks.append(task)
    save_tasks(path, tasks)
    return "Task added successfully"


def view_tasks(tasks):
    print(color_text("Your Tasks:", Colors.INFO))
    if not tasks:
        print(color_text("No tasks available", Colors.ERROR))
        return
    for i, task in enumerate(tasks, start=1):
        print(color_text(f"{i}. {task}", Colors.SUCCESS))


def remove_task(tasks, path):
    try:
        num = int(input(color_text("Enter task number to delete: ", Colors.QUESTION)))
    except ValueError:
        return "Invalid number"

    if 0 < num <= len(tasks):
        tasks.pop(num - 1)
        save_tasks(path, tasks)
        return "Task deleted successfully"
    else:
        return "Invalid number"


def delete_all_tasks(tasks, path):
    if not tasks:
        return "No tasks to delete"

    confirm = input(color_text("Delete all tasks? (y/n): ", Colors.QUESTION)).strip().lower()
    if confirm not in ("y", "yes"):
        return "Delete all canceled"

    tasks.clear()
    save_tasks(path, tasks)
    return "All tasks deleted successfully"

#entry of program
def main():
    tasks = load_tasks(file_path)
    toast_message = ""

    while True:
        clear_terminal()
        display_menu(toast_message)
        toast_message = ""
        try:
            choice = int(input(color_text("Enter choice: ", Colors.QUESTION)))
        except ValueError:
            toast_message = "Invalid choice"
            continue

        match choice:
            case 1:
                toast_message = add_task(tasks, file_path)
            case 2:
                view_tasks(tasks)
                input(color_text("\nPress Enter to continue...", Colors.QUESTION))
            case 3:
                toast_message = remove_task(tasks, file_path)
            case 4:
                toast_message = delete_all_tasks(tasks, file_path)
            case 5:
                break
            case _:
                toast_message = "Invalid choice"


if __name__ == "__main__":
    main()