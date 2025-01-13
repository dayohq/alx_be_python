# define numbers and operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ")

# creat arithmetic function
def perform_operation(num1, num2, operation):
    """Perform basic arithmetick operations based on the provided parameters.
    
    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        opeation (str): The operation to perform ('add', 'subtract', 'multiply', and 'divide')
    
    Returns:
        float: The result of the operation, or
        str: A message in case of invalid operation or division by zero.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."

