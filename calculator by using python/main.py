#program to make simple calculator
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def power(x,y):
    return pow(x,y)

print ("select operation.")
print ("1.ADD")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
choice = input("enter choice(1/2/3/4/5):")
num1 = int (input("enter the first number"))
num2 = int (input("enter the second number"))
if choice =='1':
    print('Addition is :',add(num1,num2))
if choice =='2':
    print('subtraction is :',subtract(num1,num2))
if choice =='3':
    print('multiplication is:',multiply(num1,num2))
if choice =='4':
    print('Division is:',divide(num1,num2))
if choice =='5':
    print('Power is :',power(num1,num2))
else:
    print('not found')