# Guide to the project

## Introduction
This project was to create a function that would look at the factors of an integer, and return keywords based on specific factors being present.
If the input number was a multiple of 3, 5 or 7 it would return "pling", "plang" or "plong" respectively. If the input number had none of these factors it would return the number.

### Examples
- If the number 18 (2 * 3 * 3) was input then the function should return "pling".
- If the number 21 (3 * 7) was input then the function should return "plingplong".
- If the number 32 (2 * 2 * 2 * 2 * 2) was input then the function should return 32, as none of the key factors are present.
- If the string "Hello world" was input then the function should inform the user to use numbers, and not crash.
- If the decimal number 2.57 was input then the function should inform the user to only use integers, not decimals.

### Contents
####Key files
- factorfunction - the key function that runs the operation.
- inttester - an abstracted part of the code to check if the value passed into the function was an integer.
- factorinput - a script that allows the user to input a number directly and prints the result.
- factor test - a series of tests that ensure the function is performing properly.

#### Other files
- factorfunctionlegacy - an old version of the function that does not allow float inputs. 
- worklog - a record of the process while working on the project.
- guide - this file.

### Usage
To call the function first run " from factorfunction import * ". The function can now be called as factorfunction(input). This will then run the function and return the appropriate string for the input. The function accepts integers; floats that are equivalent to integers, such as 3.00; and strings that are equivalent to integers, such as "15". 

If the user wants to input numbers into the terminal, they can run the "factorinput" script, which will give them a prompt to input a number.

#### Notes

The factorfunctionlegacy is a lighter weight version of factorfunction, requiring 16 less operations, and can be used instead when floats of the form 21.0 want to be disgarded, rather than accepted as 21. The file will still disgard 3.14 as normal.