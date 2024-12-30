Task = input("Enter task description: ")
Priority = input("Enter the task priority (high, medium, low): ")
Time_Bound = input("Is task time-bound? (yes or no): ")


match Priority:
    case "high":
        reminder = f"The task {Task} is of high priority."
    case "medium":
        reminder = f"The task {Task} is of medium priority."
    case "low":
        reminder = f"The task {Task} is of low priority."
    case _:
        reminder = f"The task {Task} has an unspecified priority."
    
if Time_Bound == "yes":
    reminder += " It requires immediate attention today!"
elif Time_Bound != "no":
    print("\nInvalid time-bound input. Please enter yes or no.")
    reminder = "No reminder generated due to invalid input."

print("\nDaily reminder:")
print(reminder)
