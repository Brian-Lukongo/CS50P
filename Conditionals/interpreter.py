# This program is an interpreter for simple arithmetic expressions. The user will enter an expression in the form of "x y z", where x and z are numbers and y is an operator (+, -, *, /). The program will evaluate the expression and output the result. The result will be formatted to one decimal place.
def main():
    
    expression = input("Expression: ")

    x_str, y, z_str = expression.split(" ")
    x = float(x_str)
    z = float(z_str)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    print(f"{result:.1f}")

main()
