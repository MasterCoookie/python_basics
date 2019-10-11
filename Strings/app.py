course = "Python Programming"
print(len(course))
# accessing cetrain character
print(course[2])
# passing negative value starts count form the end of the string
print(course[-2])
# sliceing the string [starting index included: ending index not included]
# both args are optional, passing nothing will be interpreted as 0 or length of the string
print(course[0:3])
# backslash usage in practise: (\n for new line)
message = "Python \" Codin"
print(message)
first = "jan"
last = "kocurek"
# concatonating strings, just like in js
full = first + " " + last
print(full)
# new concatonating, dont forget the f, u cant put whatever u want instide {}
full = f"   {first} {last}"
print(full)
# couple useful methods to be used on strings
# title() makes first letters uppercase
print(full.title())
# strip() deletes unnecessary spaces and etc
print(full.strip())
# find() finds the passed string index in the string that its used on
# its case sensitive
print(full.find("koc"))
#replace() is obvious
# checking for existance of a string in another string
print("jan" in full)
