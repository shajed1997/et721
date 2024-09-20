"""
Md Abu Shajed
Phython data and function
"""

print("\n------example 1: dictonary ------")
car = {
    "brand":"Tesla",
    "model":"S",
    "year": 2023,
    "last_visit" : "March, 2022"
}

print(f"Best car of 2022 = {car["brand"]}, model = {car["model"]}")

print("\n------ example 2: loop through each key in a dictionary------")
for k in car:
    print(f"{k} has a value of {car[k]}")  #print each key

print("\n------example 3: key pair in a dictionary ------")
print(f"dictionary has {len(car)} key-value pairs")

print("\n------example 4: remove a key-pair from the dictionary------")
car.pop("year")
print(f"dictionary after removing the 'year' key")
for k in car:
    print(f"{k} , {car[k]}")

print("\n------example 5: get method to get the value of the key------")
look_key = "last_visit"
print(f"The value of the key {look_key} is {car.get(look_key)} ")

print("\n------example 6: store data in a dictionary------")
phrase = "to be or not to be"
phrase = phrase.split()
print(f"phrase after the split method {phrase}")
word_count_dict = {}   #empty dictionary
for word in phrase:
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] += 1
print(word_count_dict)      

print("\n -------Excerise---------")
#given the following user list, find the number of users that use 'gmail', 'hotmail', and 'yahoo'

user =[
    'ppan@gmail.com',
    'd@hotmail.com',
    'ckent@yahoo.com',
    'bwayne@hotmail.com',
    'tstark@gmail.com',
    'shrek@gmail.com'

]
email_counts = {
    'gmail': 0,
    'hotmail': 0,
    'yahoo': 0
}
for email in user:
    email_part, domain = email.split('@')
    domain_name = domain.split('.')[0]
    
    if domain_name in email_counts:
       email_counts[domain_name] += 1

print("Gmail users:", email_counts['gmail'])
print("Hotmail users:", email_counts['hotmail'])
print("Yahoo users:", email_counts['yahoo'])