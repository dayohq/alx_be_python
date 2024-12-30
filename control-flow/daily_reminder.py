task = input("Enter task description: ")
priority = input("Enter the task priority (high, medium, low): ")
time_bound = input("Is task time-bound? (yes or no): ")

match priority:
    case "high":
        reminder = f"The task {task} is of high priority."
    case "medium":
        reminder = f"The task {task} is of medium priority."
    case "low":
        reminder = f"The task {task} is of low priority."
    case _:
        reminder = f"The task {task} has an unspecified priority."
    
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

print(reminder)
