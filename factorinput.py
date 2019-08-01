## this script allows the user to run the function "factors" using prompted inputs

# we need to import our function to run it
from factorfunctionlegacy import *
# we run a print statement to request the user to input a number

print("please input the number to test")

# fetch the input as a string, but format it to be an int so we can run the function on it
print(functionfactor(input("number = ")))