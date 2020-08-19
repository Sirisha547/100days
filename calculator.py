def add(a,b):
    return(a+b)
def subtraction(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def division(a,b):
    return(a/b)
print("select operator")
print("1.add")
print("2.subtraction")
print("3.multiply")
print("4.division")
while True:
    choice=input("enter choice(1/2/3/4): ")
    if choice in ('1','2','3','4'):
        a=int(input("enter a number:"))
        b=int(input("enter a number:"))
        if choice=='1':
            print(a,"+",b,"=",add(a,b))
        elif choice=='2':
            print(a,"-",b,"=",subtraction(a,b))
        elif choice=='3':
            print(a,"*",b,"=",multiply(a,b))
        elif choice=='4':
            print(a,"/",b,"=",division(a,b))
        break
    else:
        print("invalid output")
