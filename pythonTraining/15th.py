english =float(input("Enter english marks:"))
math =float(input("Enter math marks:"))
computers=float(input("Enter computers marks:"))
physics =float(input("Enter physics marks:"))
chemistry =float(input("Enter chemistry marks:"))
if english>100 and math>100 and computers>100 and physics>100 and chemistry>100:
    print("One of the marks greater than 100")
else:
    total= english+math+computers+physics+chemistry
    percentage= (total/500)*100
    print("Total Marks =%.2f "  %total) 
    print("Marks Percentage = %.2f"  %percentage)
    if(percentage>=90):
        print("A Grade")
    elif(percentage >=80):
        print("B Grade")
    elif(percentage >=70):
        print("C Grade")
    elif(percentage >=60):
        print("D Grade")
    elif(percentage >=40):
        print("E Grade")
