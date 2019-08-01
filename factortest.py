# This file tests the function and ensures all inputs are working correctly

from factorfunction import *

print("Testing the function with various inputs, all the results are manually created")

print("Testing the basic operations, only returning single answers")
print(functionfactor(3) == "pling")
print(functionfactor(5) == "plang")
print(functionfactor(7) == "plong")
print(functionfactor(11) == "11")

print("Testing composite numbers to see output")
print(functionfactor(15) == "plingplang")
print(functionfactor(21) == "plingplong")
print(functionfactor(35) == "plangplong")
print(functionfactor(105) == "plingplangplong")

print("Testing a series of 10 random numbers to ensure code is functional")

print(functionfactor(96) == "pling")
print(functionfactor(88) == "88")
print(functionfactor(84) == "plingplong")
print(functionfactor(64) == "64")
print(functionfactor(57) == "pling")
print(functionfactor(68) == "68")
print(functionfactor(70) == "plangplong")
print(functionfactor(8) == "8")
print(functionfactor(89) == "89")
print(functionfactor(65) == "plang")

print("Testing inputs that should work, integer values as strings and floats")
print(functionfactor("70") == "plangplong")
print(functionfactor("28") == "plong")
print(functionfactor(15) == "plingplang")
print(functionfactor(15.0) == "plingplang")

print("Testing inputs that shouldn't work, non integer values")
print(functionfactor("hello world") == "error in input, please ensure only a whole number is used")
print(functionfactor("sixteen") == "error in input, please ensure only a whole number is used")
print(functionfactor(3.14) == "error in input, please ensure only a whole number is used")
print(functionfactor(-2.57) == "error in input, please ensure only a whole number is used")

