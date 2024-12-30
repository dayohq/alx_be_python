task = input("Enter task description: ")
priority = input("Enter the task priority (high, medium, low): ")
time_bound = input("Is it time-bound? (yes or no): ")


match priority:
    case "high":
        reminder = f"The task {task} is a high priority task"
    case "medium":
        reminder = f"The task {task} is a medium priority task"
    case "low":
        reminder = f"The task {task} is a low priority task"
    case _:
       print("Specify task priority")
    
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    print()
    
print(reminder)