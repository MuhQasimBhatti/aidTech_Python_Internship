class Task:
    def __init__(self, title, description, status="Not Done"):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid index")

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index+1}. [{task.status}] {task.title}: {task.description}")

    def save_tasks(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.title}\n")
                file.write(f"{task.description}\n")
                file.write(f"{task.status}\n")
                file.write("=====\n")

    def load_tasks(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                index = 0
                while index < len(lines):
                    title = lines[index].strip()
                    description = lines[index + 1].strip()
                    status = lines[index + 2].strip()
                    self.tasks.append(Task(title, description, status))
                    index += 4
        except FileNotFoundError:
            print("File not found.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Quit")
        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            print("\n*** Tasks ***")
            todo_list.view_tasks()
        elif choice == "4":
            filename = input("Enter file name to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == "5":
            filename = input("Enter file name to load tasks from: ")
            todo_list.load_tasks(filename)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
