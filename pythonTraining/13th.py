start=int(input("Enter start range:"))
end =int (input("Enter end range:"))
if start>end:
    print("start value should be less than end value")
else:
    for i in range(start,end):
        print(i)
