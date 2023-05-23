class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def update_details(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_all_tasks(self):
        for task in self.tasks:
            print(f"Title: {task.title}\nDescription: {task.description}\nDue Date: {task.due_date}\nCompleted: {task.completed}\n")

    def view_incomplete_tasks(self):
        for task in self.tasks:
            if not task.completed:
                print(f"Title: {task.title}\nDescription: {task.description}\nDue Date: {task.due_date}\n")

    def view_completed_tasks(self):
        for task in self.tasks:
            if task.completed:
                print(f"Title: {task.title}\nDescription: {task.description}\nDue Date: {task.due_date}\n")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

# Main program
def main():
    todo_list = TodoList()
    while True:
        print("Todo List Options:")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Incomplete Tasks")
        print("4. View Completed Tasks")
        print("5. Mark Task as Completed")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date: ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            todo_list.view_all_tasks()

        elif choice == "3":
            todo_list.view_incomplete_tasks()

        elif choice == "4":
            todo_list.view_completed_tasks()

        elif choice == "5":
            task_index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_task_completed(task_index)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
