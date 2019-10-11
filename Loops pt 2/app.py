# instead of "flag" method we can use for else in python
names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
# the else statment will be executed if the loop wasn't broken at any point
else:
    print("Not found")
