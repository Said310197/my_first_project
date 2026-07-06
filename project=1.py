
def calculator(a,b,op):
    try:
        if op == "+":
            return a + b 
        if op == "-":
            return a - b 
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                return a / b
    except ValueError:
        print("error you most write number not 0")

try:
    a = float(input("write number one"))
    
except:
    print("online number")
try:

    b = float(input("write number two"))
except:
    print("online number 2")
try:
    op = input("write skil! + , - , * , / ")
except ValueError:
    print("+ - * /")

s = calculator(a,b,op)
print(s)



