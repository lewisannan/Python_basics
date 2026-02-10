try:
    firstnumber = float(input("Enter first number:"))
    operator = input("Enter operator:")
    secondnumber = float(input("Enter second number:"))

    if operator == "+":
        results = firstnumber + secondnumber
        print(results)
    elif operator == "-":
        results = firstnumber - secondnumber
        print(results)
    elif operator == "*":
        results = firstnumber * secondnumber
        print(results)
    elif operator == "/":
        if secondnumber == 0:
            print("Division by zero is not allowed.")
        results = firstnumber / secondnumber
        print(results)
    else:
        print("INVALID OPERATOR")
        print("Try using these operators:+ - * /")
except :
    print("Please use valid numbers only eg:",36,80,-982)







