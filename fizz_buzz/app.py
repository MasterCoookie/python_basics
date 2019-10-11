def fizz_buzz(input):
    by3 = False
    by5 = False

    if(input != 0):
        if(input % 3 == 0):
            by3 = True

        if(input % 5 == 0):
            by5 = True

        message = ""
        if(by3):
            message = "Fizz"

        if (by5):
            message += "Buzz"

    if(not by3 and not by5):
        message = input

    return message


print(fizz_buzz(15))
