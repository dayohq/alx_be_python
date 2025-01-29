import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main funtion to handle command line arguments for division.
    """
    # Ensure correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    #Extract numerator and denominator from command line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform the division using safe_divide
    result = safe_divide(numerator, denominator)

    #Print the result
    print(result)

if __name__ == "__main__":
    main()
    