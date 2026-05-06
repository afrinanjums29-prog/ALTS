def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)
print("Welcome")
flag="y"
while (flag=="y"):
    print("1-Add")
    print("2-subtraction")
    print("3-Multiplication")
    print("4-Division")
    print("5-Exit")
    choice=int(input("Enter your choice:"))
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))     
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mul()
    elif choice==4:
        div()
    else:
        print("Good Byee!!!!")
    flag=input("Do you want to continue(y/n):")
    print(flag)
    if(flag=="n"):
        print("Thank you")
        
    
