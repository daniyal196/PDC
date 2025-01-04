def result(a: int, op: str, b: int):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "/":
            return a / b if b != 0 else "Division by zero error"
        case "*":
            return a * b
        case "%":
            return a % b

a = int(input("Enter the first number: "))
op = input("Enter the operator (+, -, *, /, %): ")
b = int(input("Enter the second number: "))


print("The result is:", result(a, op, b))