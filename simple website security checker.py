z = (input("enter the website :"))
x: int = len(z)
while x >= 13:
    x = x + 1
    if z.startswith('https://'):
        print("fully secured")
        break
    else:
        print("not secure at all")
        break
#print('this is not a website ')
