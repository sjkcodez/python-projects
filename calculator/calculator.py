import math

def add(a, b):
    print(f"\n {a} + {b} is ", end="")
    return a + b

def subtract(a, b):
    print(f"\n {a} - {b} is ", end="")
    return a - b

def multiply(a, b):
    print(f"\n {a} x {b} is ", end="")
    return a * b

def divide(a, b):
    print(f"\n {a}/{b} is ", end="")
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    print(f"\n {a} mod {b} is ", end="")
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b

def power(a, b):
    print(f"\n {a} exponent {b} is ", end="")
    return pow(a, b)

def roots(a, b):
    print(f"\n {b}th root of {a} is ", end="")
    return a**(1/b)

# Main program
def calculator():
    while True:
        print("\nWelcome to Calculator")
        print("Choose one operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. power")
        print("7. roots")
        print("e. Exit")

        choice = input("Select your choice: ")

        if choice == 'e':
            print("Exiting Calculator Application. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                num1 =  int(input(f"Enter first number: "))
                num2 = int(input("Enter second number: "))

            except ValueError:
                print("Error: Please enter valid numbers.")
                continue

            if choice == '1':
                print( add(num1, num2))
            elif choice == '2':
                print( subtract(num1, num2))
            elif choice == '3':
                print( multiply(num1, num2))
            elif choice == '4':
                print( divide(num1, num2))
            elif choice == '5':
                print( modulus(num1, num2))
            elif choice == '6':
                print( power(num1, num2))
            elif choice == '7':
                print( roots(num1, num2))
        else:
            print("Error: Invalid choice. Please try again.")

calculator()
