def cal(x, y):
    quo = x / y
    rem = x % y
    return quo, rem

def main():
    try:
        num1, num2 = map(float, input("Enter two numbers: ").split())
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return

        quo, rem = cal(num1, num2)

        print(f"The quotient is: {quo:.2f}")
        print(f"The remainder is: {rem:.0f}")
    except ValueError:
        print("Invalid input. Please enter two numeric values separated by space.")

main()