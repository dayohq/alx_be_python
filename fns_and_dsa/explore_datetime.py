from datetime import datetime, timedelta

# define current date and time function
def display_current_datetime():
    """displays the current date and time in the format YYYY-MM-DD HH:MM:SS."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date(days):
    """Calculates and prints the future date after adding the given number of days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date after {days} days: {formatted_future_date}")

# Display current date and time
display_current_datetime()

# Prompt user for number of days and calculate future date
try:
    days = int(input("Enter the number of days to add: "))
    calculate_future_date(days)
except ValueError:
    print("Invalid input. Please enter an integer value.")