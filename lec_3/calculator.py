def calculator(expression):
    try:
        operators = ["+", "-", "*", "/"]
        operator = None

        for op in operators:
            if op in expression:
                operator = op
                break
        if operator is None:
                return "Unsupported operator or invalid expression"

        num1, num2 = map(float, expression.split(operator))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Division by zero is not allowed"
            result = num1 / num2

        return result

    except ValueError:
        return "Please enter valid numbers."
    
user_input = input("Enter an expression: ")
result = calculator(user_input)
print(f"Result is : {result}")
