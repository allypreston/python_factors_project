# this function takes an input number, then checks if it is a multiple of 3, 5 or 7 and
# returns keywords based on the factors, if none of the factors are met then the number
# itself is returned


# define the function, with the input of the number
def functionfactor(numbertotest):
    output = ""
        # run the modulus argument on the number for 3, check if it gives no remainder
    if numbertotest % 3 == 0:
        # if true add the string to our output placeholder
        output += "pling"

    # run the modulus argument on the number for 5, check if it gives no remainder
    if numbertotest % 5 == 0:
        # if true add the string to our output placeholder
        output += "plang"

    # run the modulus argument on the number for 7, check if it gives no remainder
    if numbertotest % 7 == 0:
        # if true add the string to our output placeholder
        output += "plong"

    # if we have no factors of 3, 5 or 7 in our number we need to return the number itself
    # checks if our string is empty
    if output == "":
        # if empty then set output to our original number, as a string
        output = str(numbertotest)

    # print to display the output
    return output
