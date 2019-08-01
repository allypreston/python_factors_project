numbertotest = input("number")
numbertotest = int(numbertotest)
# if the number is an integer run the code
# we now create a blank variable to hold our output
output = ""

# run the modulus argument on the number for 3, check if it gives no remainder
try:
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
    print(output)

except:
    # if not an integer then return a helpful output
    print("error in input, please ensure only a whole number is used")

