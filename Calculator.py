def calculator(numb1, op, numb2):
    numb1 = float(numb1)
    numb2 = float(numb2)

    if op == "+":
        print("The result is: " + str(numb1 + numb2))
    elif op == "-":
        print("The result is: " + str(numb1 - numb2))
    elif op == "/":
        print("The result is: " + str(numb1 / numb2))
    elif op == "*":
        print("The result is: " + str(numb1 * numb2))
    else:
        print("Invalid operator.")