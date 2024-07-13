def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def main():
    print("\n" + "="*60)
    print(" " * 20 + "SIMPLE CALCULATOR")
    print("="*60 + "\n")

    print(" The List Operation:")
    print("\n" + "-"*60 + "\n")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("\n" + "-"*60 + "\n")

    operation = input("CHOOSE THE OPERATION: ")
    print("\n" + "-"*60 + "\n")

    if operation in {'1', '2', '3', '4'}:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("\n" + "-"*60 + "\n")

            if operation == '1':
                print("ADDITION")
                result = add(num1, num2)
                operation_sign = '+'
            elif operation == '2':
                print("SUBTRACTION")
                result = subtract(num1, num2)
                operation_sign = '-'
            elif operation == '3':
                print("MULTIPLICATION")
                result = multiply(num1, num2)
                operation_sign = '*'
            elif operation == '4':
                print("DIVISION")
                result = divide(num1, num2)
                operation_sign = '/'

            print(f"Result of {num1} {operation_sign} {num2} = {result}")
            print("\n" + "="*60)

        except ValueError:
            print("Error: Please enter valid numbers.")
    else:
        print("Invalid input. Please enter a valid operation choice.")

if __name__ == "__main__":
    main()
