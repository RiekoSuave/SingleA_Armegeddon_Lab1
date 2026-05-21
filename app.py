def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

while True:
    print("\n=== Calculator Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = add(num1, num2)

        print("Answer:", result)

    elif choice == "2":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = subtract(num1, num2)

        print("Answer:", result)

    elif choice == "3":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Answer:", multiply(num1, num2))

    elif choice == "4":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Answer:", divide(num1, num2))
    
    
    
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")

     