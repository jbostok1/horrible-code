# This is going to be a simple calculator, you can add, subtract, multiply, and divide!

# Function for adding
def add(x, y):
    return x + y

# Function for subtracting
def subtract(x, y):
    return x - y

# Function for multiplying
def multiply(x, y):
    return x * y

# Function for dividing
def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x / y

# This is going to be the main function
def calculator():
    while True:
        try:
            # Input numbers and operations
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operation you want to perform (+, -, *, /): ")
            
            operations = {
                '+': add,
                '-': subtract,
                '*': multiply,
                '/': divide
            }

            if operator in operations:
                result = operations[operator](num1, num2)
                print(f"{num1} {operator} {num2} = {result}")
            else:
                print("Invalid operator")

        except ValueError as e:
            print(f"Invalid input: {e}")

        repeat = input("Do you want to perform another operation? (y/n): ")

        if repeat.lower() != "y":
            break

# Run calculator
calculator()
