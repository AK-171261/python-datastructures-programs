# lcm
import sys


def lcm(num1, num2, val1, val2):
    if num1 == num2:
        print(num1)
        sys.exit(1)
    else:
        if num1 < num2:
            lcm(num1 + val1, num2, val1, val2)
        elif num1 > num2:
            lcm(num1, num2 + val2, val1, val2)


if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    value1 = num1
    value2 = num2
    lcm(num1, num2, value1, value2)
