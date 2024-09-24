while True:
    a = input("num1: ")
    b = input("num2: ")
    o = input("operator: ")

    if o == "+":
        print(float(a) + float(b))
    elif o == "-":
        print(float(a) - float(b))
    elif o == "*":
        print(float(a) * float(b))
    elif o == "/":
        if float(b) == 0:
            print("Cannot divide by zero")
        else:
            print(float(a) / float(b))
    else:
        print("bad operator")

    again = input("Again? (y/n): ")
    if again == "y":
        continue
    else:
        break