from tkinter import *
from tkinter import messagebox

# Global variables to manage tasks
tasks = []
task_counter = 1

def show_error(message):
    """Displays an error message in a messagebox."""
    messagebox.showerror("Error", message)

def validate_task_entry():
    """Checks if the task entry field is empty."""
    if not task_entry.get():
        show_error("Task entry cannot be empty.")
        return False
    return True

def clear_task_entry():
    """Clears the task entry field."""
    task_entry.delete(0, END)

def add_task():
    """Adds a task to the list and updates the text area."""
    global task_counter
    
    if not validate_task_entry():
        return
    
    task = task_entry.get() + "\n"
    tasks.append(task)
    task_display.insert(END, f"[ {task_counter} ] {task}")
    task_counter += 1
    clear_task_entry()

def remove_task():
    """Removes a task based on the task number and updates the text area."""
    global task_counter
    
    if not tasks:
        show_error("No tasks to remove.")
        return

    try:
        task_num = int(task_number_entry.get(1.0, END).strip())
        if task_num < 1 or task_num > len(tasks):
            show_error("Invalid task number.")
            return
    except ValueError:
        show_error("Invalid input. Please enter a number.")
        return

    tasks.pop(task_num - 1)
    task_counter -= 1
    task_display.delete(1.0, END)

    for i, task in enumerate(tasks, start=1):
        task_display.insert(END, f"[ {i} ] {task}")

    task_number_entry.delete(1.0, END)

def exit_app():
    """Exits the application."""
    root.destroy()

# Main application setup
if __name__ == "__main__":
    root = Tk()
    root.title("To-Do List")
    root.geometry("300x350")
    root.configure(bg="light blue")

    # UI components
    Label(root, text="Enter Task", bg="light blue").grid(row=0, column=1, pady=5)
    task_entry = Entry(root, width=30)
    task_entry.grid(row=1, column=1, padx=10)

    Button(root, text="Add Task", command=add_task, bg="light green").grid(row=2, column=1, pady=5)

    task_display = Text(root, height=10, width=40)
    task_display.grid(row=3, column=1, padx=10, pady=10)

    Label(root, text="Task Number", bg="light blue").grid(row=4, column=1, pady=5)
    task_number_entry = Text(root, height=1, width=5)
    task_number_entry.grid(row=5, column=1, padx=10)

    Button(root, text="Remove Task", command=remove_task, bg="light coral").grid(row=6, column=1, pady=5)
    Button(root, text="Exit", command=exit_app, bg="light coral").grid(row=7, column=1, pady=10)

    root.mainloop()
