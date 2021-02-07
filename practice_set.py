#1. WAP to find out the greatest number (FROM USER) :
# num1 = int(input("input 1st number : "))
# num2 = int(input("input 2nd number : "))
# num3 = int(input("input 3rd number : "))
# num4 = int(input("input 4th number : "))

# if(num1>num2):
#     f1 = num1
# else:
#     f1 = num2

# if(num3>num4):
#     f2 = num3
# else:
#     f2 = num4

# if(f1>f2):
#     print(str(f1) + " is greatest")
# else:
#     print(str(f2) + " is greatest")

#2. Student pass or fail (>40% or at least 33% in each subject)(3 subjects)
# sub1 = int(input("enter marks of 1st subject :\n"))
# sub2 = int(input("enter marks of 2nd subject :\n"))
# sub3 = int(input("enter marks of 3rd subject :\n"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("you failed cz of less than 33% marks in or any subjet(s)")
# elif(sub1 + sub2 + sub3)/3<40:
#     print("failed, grand total is less than 40%")
# else:
#     print("you passed !!")

#3. ---spam content identifier for mentioned keywords (make a lot money, buy now, sbscribe this, click this)
# sentance = str(input("enter your text :\n"))
# if("buy now" in sentance):
#     spam = True
# elif ("make lot of money" in sentance):
#     spam = True
# elif ("click this" in sentance):
#     spam = True
# elif ("subscribe this" in sentance):
#     spam = True
# elif ("subscribe" in sentance):
#     spam = True
# else:
#     spam = False
# if(spam):
#     print("This is a SPAM !")
# else:
#     print("This is not a SPAM !")

#4. Grading system 90-100=excelent, 80-90=a, 70-80=b, 60-70=c, 50-60=d, >50--fail
marks = int(input("please enter yous marks: "))
if(marks>=90):
    print("Excellent")
elif(marks>=80):
    print("A Grade")
elif(marks>=70):
    print("B Grade")
elif(marks>=60):
    print("C Grade")
elif(marks>=50):
    print("D Grade")
else:
    print("Fail")

#Another method
# marks = int(input("please enter your marks: "))
# if marks>=90:
#     grade = "Excellent"
# elif marks>=80:
#     grade = "A"
# elif marks>=70:
#     grade = "B"
# elif marks>=60:
#     grade = "C"
# elif marks>=50:
#     grade = "D"
# else:
#     grade = "FAIL !"
# print("Your Grade is : " + grade)

