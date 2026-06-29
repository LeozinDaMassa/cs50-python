def main():
    # Takes User Input
    expression = str(input("Expression:"))
    # takes user input and assigns to variables
    x, y, z = expression.split(" ")
    # converts values into an integer
    x = int(x)
    z = int(z)
    # y is +, -, *, or / 
    if y == "+" :
        soma = (x + z)
        print(f"{soma:.1f}")
    elif y == "-" :
        subtrair = (x - z)
        print(f"{subtrair:.1f}")
    elif y == "*" :
        multipli = (x * z)
        print (f"{multipli:.1f}")
    elif y == "/" :
        divid = (x / z)
        print(f"{divid:.1f}")

main()

