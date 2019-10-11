# input, self explenatory
age = input("Whats your age? ")

# needs to be converted into int so we can work on it
age = int(age)

# if's and else's are quite different
if age >= 18:
    print("Adoult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# logical operator
name = input("What's your name? ")
# using strip() to get rid of empty spaces
if not name.strip():
    print("Name is empty!")

# code below shows how python simplyfies logical operators
if 18 <= age < 65:
    message = "Eliglable"
else:
    message = "Not eliglable"

print(message)
# insted of age >= 18 && age < 65

# this can be simplyfied even more, almost written in plain english

message = "Eliglable" if 18 <= age < 65 else "Not eliglable"

print(message)
