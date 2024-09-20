"""
Md Abu Shajed
Sept 20, 2024 Python Classes
"""

print("\n-------Example 1: exception handling-----\n")
def hour_ratio():
    try:
        hours = 24
        h = int(input("Please enter a number to divide 24 hours: "))

        hours /=h #hours = hours/h
        return hours
    except ZeroDivisionError:
        print(f"The number {h} can't be divided by 24. Result is undefined")
    except ValueError:
        print(f"Input value was not a number.")
    except:
        print(f"Program has an error.")


print(hour_ratio())
print("\n =============End of program================\n")


print("\n-------Example 2: classes-----\n")
#define a class named 'complex'
class Complex:
    def __init__(self, realpart, imgpart):
        self.r = realpart
        self.i = imgpart
# create an instance of the class
point1 = Complex(3.0, -4.5)

# calling the instance object
real1 = point1.r
imag1 = point1.i

# prompt result
print(f"real number = {real1} with imaginary number = {imag1} ")        

print("\n =============End of program================\n")


print("\n-------Example 3: Attributes and Methods-----\n")
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
#method of class car
    def get_descriptive_name(self):
        full_name = f"{self.year}, {self.make}, {self.model}"
        return full_name
    
#method 2: read and print the odometer
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")       
        
#method 3: update and print odometer
    def update_odometer(self,mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
        
#method 4: increment odometer
    def increment_odometer(self,miles):
        self.odometer_reading += miles
        
#create an instance of class car
usercar1 = Car("audi", "a4", 2020)

#access the attributes
print(usercar1.year)

#access the method
print(usercar1.get_descriptive_name())
usercar1.read_odometer()
usercar1.update_odometer(100)
print(usercar1.read_odometer())


print("\n-------Exercise-----\n")
"""
Md Abu Shajed
Lab 6 Excerise  
"""

class BankAccount:
    def __init__(self, account_number, account_holder):
        # Initialize account number, account holder, and balance
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0  # Balance is initialized to 0.0

    def deposit(self, amount):
        # Adds the specified amount to the balance
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Subtracts the specified amount from the balance if sufficient funds exist
        if amount > self.balance:
            print("Insufficient balance for the withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

# Example usage
account = BankAccount("123456789", "John Doe")
account.deposit(500)
account.withdraw(100)
account.withdraw(600)

        