"""
Md Abu Shajed
Sep 30, unit testing 'input' data
"""
def main():
    # loop  to collect  number of students
    while True:
        try:
            num_students = int(input("Enter the number of students"))
            if num_students >0:
                break
            else:
                print("Invalid input.")




        except ValueError:
            print("Invalid input. Try again.")
    # nested loop to collect the grade for each students
    totalsumgrade = 0
    for i in range(num_students):
        while True:
            try:
                grade = int(input("Enter a grade for student{i+1}"))
                if 0<= grade <=100:
                    totalsumgrade += grade
                    break
                else:
                    print("Grade must be between 0 to 100.")
            except ValueError:                    
                print("Invalid input")  
    average = totalsumgrade / num_students
    print(f"The class average is {average:.2f}\n")                  


if __name__ == "__main__":
    main()


 



