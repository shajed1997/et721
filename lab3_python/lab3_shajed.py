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



 print  ("-----example 2: Loops ---------")
SECRET = 8
userguess = int (input("Gues a  number between 1 and 10: "))
while not (SECRET ==userguess):
    usergueess = int(input ("wrong guess. guess again:"))


print (f"Congrats! {userguess} is the right number!")
print("-------examole :3 Loops, break statement ---------")
blance =1000
widthdraw =0
deposit =0
while True:
    userinput =input("Do you want to widthdraw, w, or deposit, d?")
    if userinput == 'w' or userinput =='w':
        w_amount = int(input('How much do you want to widthdraw?'))
        if w_amount>balance:
            print(f"unsuficient funds! you can't widthdraw more than{balance}")
        else:
            balance -= w_amount    


    elif  userinput == 'd' or userinput =='D':
       
          d_amount = int (input('How much do you want to deposit?'))
          balance += d_amount
          print(f"your new balance is {balance}")  
    else:
        print("Invalid selection!")  
    choice = Input ("would you like to do another transaction?(y,n)")  
    if not(choice=='y' or choce== 'Y')  
       break
print("Thank you for banking with us!")  


print("-----example 4: for loop as a counter --------")


for n in range(-5,3,2):
    print(f"counting = {n}")


print ("-----example 5: for loop in a list")  
colours = ['magenta','babyblue';'olive']


for c in colors:
    print(f"color = {c}")





