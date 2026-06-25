def main():
    operation = input("Enter an operation (sum, sub, mult, square): ")

    if operation == "sum":
        sum()
    elif operation == "sub":
        sub()
    elif operation == "mult":
        mult()
    elif operation == "square":
        square()

def sum():
    x = int(input("Enter an ammount: "))
    y = int(input("Enter a second ammount: "))
    print('The sum result is', x + y)

def sub():
    x = int(input("Enter an ammount: "))
    y = int(input("Enter a second ammount: "))
    print('The difference is', x - y)

def mult():
    x = int(input("Enter an ammount: "))
    y = int(input("Enter a second ammount: "))
    print('The multiplication result is', x * y)

def square(n):
    return pow(n, 2)

main()