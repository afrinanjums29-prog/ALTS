def add():
    a=10
    b=20
    print(a+b)
def sub():
    a=10
    b=20
    print(a-b)
def mul():
    a=10
    b=20
    print(a*b)
def div():
    a=10
    b=20
    print(a/b)
print("1-Add")
print("2-subtraction")
print("3-Multiplication")
print("4-Division")
print("5-Exit")
choice=int(input("Enter your choice:"))
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


    
