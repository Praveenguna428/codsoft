tasks = []

def display_tasks():
	print("Tasks List:")
	for i, task in enumerate(tasks, start=1):
		print(f"{i}. {task}")
		print("-" * 60 + "\n")

# Function to add a task
def add_task():
	task = input("Enter a task: ")
	tasks.append(task)
	print("Task added!")
	print("." * 60 + "\n")

# Function to delete a task
def delete_task():
	display_tasks()
	task_number = int(input("Enter the task number to delete: ")) - 1
	if task_number >= 0 and task_number < len(tasks):
		tasks.pop(task_number)
		print("Task deleted!")
		print("." * 60 + "\n")
	else:
		print("Invalid task number.")

# Function to mark a task as completed
def complete_task():
	display_tasks()
	task_number = int(input("Enter the task number to mark as completed: ")) - 1
	if task_number >= 0 and task_number < len(tasks):
		tasks[task_number] += " [ TASK COMPLETED ]"
		print("Task marked as completed!")
		print("." * 60 + "\n")
	else:
		print("Invalid task number.")

# Main program loop
while True:
	print("\nTo-Do List Options:")
	print("1. Display Tasks")
	print("2. Add Task")
	print("3. Delete Task")
	print("4. Mark Task as Completed")
	print("5. Quit")
	print("*" * 60 + "\n")
	choice = input("Enter your choice: ")
	print("*" * 60 + "\n")
	if choice == "1":
		display_tasks()
	elif choice == "2":
		add_task()
	elif choice == "3":
		delete_task()
	elif choice == "4":
		complete_task()
	elif choice == "5":
		break
	else:
		print("Invalid choice. Please try again.")
