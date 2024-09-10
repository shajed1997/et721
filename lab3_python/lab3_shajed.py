"""
Md Abu Shajed
lab 3, python review
"""
print("-----example 1: control flow----")
labs = int(input("Enter labs' grade"))
exams = int(input("Enter exams' grade: "))
gpa =''
finalgrade = 0


if (0<=100 and 0<=exams<=100):
   finalgrade = labs+exams / 2
   gpa=''
   if (100> finalgrade>= 80):
      gpa = 'A'
   elif (90> finalgrade>=70):
       gpa ='B'
   elif (80> finalgrade>=70):
       gpa ='c'
   elif (70> finalgrade>=60):
       gpa ='D'
   elif (60> finalgrade>=0):
       gpa ='F'
   else:
      gpa ='UNDEFINED'
else: 
    gpa ='UNDEFINED' 

print(f"Your final grade for the class is {finalgrade} ={gpa}")

    if not (0<labs<=100):
        print(f"Grade for lab {labs} is invalid")
    elif  not (0<labs<=100):
         print(f"Grade for exams {exams} is invalid")
         gpa ='UNDEFINED'  


 PRINT(F"YOUR FINAL GRADE FOR THE CLASS IS {finalgrade}={gpa}")



