
def calculator(a, b, op):
    if op == "+":
        return a + b 
    elif op == "-":
        return a - b 
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error you most write number!!!"
        return a / b 
    else:
        return "error"
result = None
while True:
    print("Menu Calculator Hasan")
    print("1/.calculator.")
    print("2/calculator with save")
    print("3/calculator reset.")
    print("4/exit out calculator")

    
    choice = input("you most choice {1, 2, 3, 4}")

    if choice == "1":
        a = float(input("number one: "))
        b = float(input("number two: "))
        op = input("check (+, -, *, /)")
        result = calculator(a, b, op)
        print("your result:", result)
        print("DEBUG", result)

    elif choice == "2":
        if result is None:
            print("no result")
            continue

        b = float(input("next number:  "))
        op = input("check (+, -, *, /)")
        result = calculator(result, b, op)
        print("your result:",result)
    
    elif choice == "3":
        result = None 
        print("clearner calculator exsesus")
    
    elif choice == "4":
        print("BUY.........")
        break 
    else:
        print("ERROR 4000000")