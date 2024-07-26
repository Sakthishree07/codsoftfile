class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Added task: '{task}'")

    def complete_task(self, task):
        for t in self.tasks:
            if t['task'] == task:
                t['completed'] = True
                print(f"Completed task: '{task}'")
                return
        print(f"Task '{task}' not found")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for idx, t in enumerate(self.tasks, 1):
            status = "Completed" if t['completed'] else "Not Completed"
            print(f"{idx}. {t['task']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Options:")
        print("1. Add task")
        print("2. Complete task")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to complete: ")
            todo_list.complete_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
