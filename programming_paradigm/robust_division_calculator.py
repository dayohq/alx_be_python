def safe_divide(numerator, denominator):
    """Perform division with error handling for zero division and non-numeric inputs.
    
    Args:
    numerator (str): The numerator as a string (will be converted to float).
    denominator (str): THe denominator as a string (will be converted to float).
    
    Returns:
        str: The result of the division or an error message.
        """
    
    try:
        #convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        #perform division
        result = numerator / denominator
        return f"The result of the division is {result: .1f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    
