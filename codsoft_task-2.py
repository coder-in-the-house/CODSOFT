def add_numbers(a, b):
    """Calculate the sum of two numbers."""
    return a + b

def subtract_numbers(a, b):
    """Calculate the difference between two numbers."""
    return a - b

def multiply_numbers(a, b):
    """Calculate the product of two numbers."""
    return a * b

def divide_numbers(a, b):
    """Calculate the division of two numbers, handling division by zero."""
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

def display_menu():
    """Display the menu options to the user."""
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

def get_number(prompt):
    """Prompt the user to enter a number and handle invalid inputs."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Run the calculator application."""
    display_menu()
    
    while True:
        operation = input("Select an option (1/2/3/4): ")
        
        if operation in {'1', '2', '3', '4'}:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if operation == '1':
                result = add_numbers(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif operation == '2':
                result = subtract_numbers(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif operation == '3':
                result = multiply_numbers(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif operation == '4':
                result = divide_numbers(num1, num2)
                print(f"{num1} / {num2} = {result}")

            continue_calculation = input("Would you like to perform another calculation? (yes/no): ").strip().lower()
            if continue_calculation != "yes":
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
