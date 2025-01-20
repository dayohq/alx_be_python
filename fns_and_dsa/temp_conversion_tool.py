# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
try:
    # Get temperature input from user
    temperature = float(input("Enter the temperature: "))
    unit = input("is this in Celsius (C) or Fahrenheit (F)? ").strip().lower()

    # Convert based on user input
    if unit == "c":
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
    elif unit == "f":
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius of 'F' for Fahrenheit.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")