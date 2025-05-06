def calculate(num1, num2, operation):
    """Perform the calculation based on the operation provided."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

def main():
    # Display welcome message
    print("Welcome to the Basic Calculator!")
    print("Operations: + (addition), - (subtraction), * (multiplication), / (division)")
    
    # Get user input with clear prompts
    try:
        print("\nPlease provide the following information:")
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        print("Available operations: + (add), - (subtract), * (multiply), / (divide)")
        operation = input("Choose operation (enter +, -, *, or /): ")
        
        # Perform calculation
        result = calculate(num1, num2, operation)
        
        # Display result
        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} {operation} {num2} = {result}")
            
    except ValueError:
        print("Error: Please enter valid numbers")

if __name__ == "__main__":
    main()
