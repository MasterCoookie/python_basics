# keyword def to define a function
# a default value can be set "=1"
# arrow sets the type of value returned (not required)


def increment(number, by=1) -> tuple:
    # many values can be reutrned by a function
    return (number, number + by)


# adding a star next to a paramiter will make python see it as a tuple
def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


# the type returned is a tuple (read-only list)
print(increment(2, 3))

print(multiply(2, 3, 4, 5))


# ** args are basically an js object (a dictionary in python)
def save_user(**user):
    print(user["id"])


save_user(id=1, name="admin")
