
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def div(x,y):
    if y == 0:
        print("division is not possible")
    else:
        return x/y

def mul(x,y):
    return x*y

def pow(x,y):
    return x**y

print("----------OPERATIONS-----------")
print("1.Addition")
print("2.Subtraction")
print("3.Divition")
print("4.Multiplication")
print("5.Power")
choice =input("Enter the operation you want to perform:")

operations = {
        '1':add,
        '2':sub,
        '3':div,
        '4':mul,
        '5':pow
        }
if choice in operations:
    x=float(input("Enter the first number"))
    y=float(input("Enter the second number"))
    result=operations[choice](x,y)
    print(result)
else:
    print("Invalid choice")
