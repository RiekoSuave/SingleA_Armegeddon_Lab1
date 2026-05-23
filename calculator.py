#!/usr/bin/env python3

import math


SPECIAL_VALUES = {
    "pi": math.pi,
    "π": math.pi,
    "e": math.e
}

#various functions for our calculator
def get_number(prompt="Enter a number: "):
    """Handles normal numbers and constants like pi/e."""
    while True:
        value = input(prompt).strip().lower()

        if value in SPECIAL_VALUES:
            return SPECIAL_VALUES[value]

        try:
            return float(value)
        except ValueError:
            print("❌ Invalid input. Enter a number, 'pi', or 'e'.")


def unary_operation(operation):
    number = get_number()
    try:
        result = operation(number)
        print(f"✅ Result: {result}\n")
    except ValueError as error:
        print(f"❌ Math error: {error}\n")


def binary_operation(operation):
    first = get_number("Enter first number: ")
    second = get_number("Enter second number: ")

    try:
        result = operation(first, second)
        print(f"✅ Result: {result}\n")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero.\n")


def factorial():
    number = get_number("Enter a whole number: ")

    if not number.is_integer() or number < 0:
        print("❌ Factorial only works for non-negative integers.\n")
        return

    print(f"✅ Result: {math.factorial(int(number))}\n")


def show_menu():
    print("=" * 45)
    print("🧮 Scientific Calculator")
    print("=" * 45)

    for key, (name, _) in OPERATIONS.items():
        print(f"{key}. {name}")

    print("0. Exit")
    print("=" * 45)


OPERATIONS = {
    "1": ("Addition", lambda: binary_operation(lambda x, y: x + y)),
    "2": ("Subtraction", lambda: binary_operation(lambda x, y: x - y)),
    "3": ("Multiplication", lambda: binary_operation(lambda x, y: x * y)),
    "4": ("Division", lambda: binary_operation(lambda x, y: x / y)),
    "5": ("Exponent (x^y)", lambda: binary_operation(lambda x, y: x ** y)),
    "6": ("Square Root (√x)", lambda: unary_operation(math.sqrt)),
    "7": ("Log Base 10 (log)", lambda: unary_operation(math.log10)),
    "8": ("Natural Log (ln)", lambda: unary_operation(math.log)),
    "9": ("Sine (sin)", lambda: unary_operation(math.sin)),
    "10": ("Cosine (cos)", lambda: unary_operation(math.cos)),
    "11": ("Tangent (tan)", lambda: unary_operation(math.tan)),
    "12": ("Modulus (%)", lambda: binary_operation(lambda x, y: x % y)),
    "13": ("Factorial (!)", factorial),
    "14": ("Absolute Value", lambda: unary_operation(abs)),
}


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("👋 Goodbye!")
            break

        action = OPERATIONS.get(choice)

        if action:
            print(f"\n🔹 {action[0]}")
            action[1]()
        else:
            print("❌ Invalid option. Try again.\n")


if __name__ == "__main__":
    main()