# Function to get valid input from user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))  # Try to convert input to a float
        except ValueError:
            print("Invalid input! Please enter a valid number.")  # If invalid, show an error and prompt again

# Taking input from the user
num1 = get_number("Enter first number - ")
num2 = get_number("Enter second number  ")

# Multiplying the numbers
product = num1 * num2

# Displaying the result
print(f"The product of {num1} and {num2} is: {product}")
