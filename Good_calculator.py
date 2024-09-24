def calculator():
    while True:
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            operator = input("Enter operator: please use (+,-,*,/): ")

            # Perform the calculation!
            if operator == '+':
                result = number1 + number2
            elif operator == '-':
                result = number1 - number2
            elif operator == '*':
                result = number1 * number2
            elif operator == '/':
                if number2 == 0:
                    print("Can't divide by zero")
                    continue
                result = number1 / number2
            else:
                print("Invalid operator")
                continue

            # Print the result
            print("Result: ", result)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

        # Ask if the user wants to perform another calculation
        repeat = input("Do you want to continue? (y/n) ")
        if repeat.lower() != 'y':
            break

calculator()
