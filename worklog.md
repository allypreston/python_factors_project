# Documentation of steps in the development process

## - 1 creating the function
initially the function was created to check the factors of the number and append the relevant parts to the output, returning the values as appropriate
blockers - none


## - 2 creating input file
created an input file to allow use of the created function

blockers
- inputs are not always appropriate integers > fixed with use of try:

## - 3 creating tests
created a file with several basic tests to see if the function worked as expected

blockers
- test didn't work with floats, rounded them instead of discarding > fixed by first casting as a string
- test didn't work with output being returned initially > fixed by using print for the function

## - 4 improving input checking
wanted to have the function allow floats of the format 15.0 as 15, as this makes logical sense to do

blockers
- file became bloated > abstracted the file to ensure it wasnt too heavy
- test was failing as it was still running off the legacy function

## - 5 created readme file
wanted a readme file to aid users in their use of the function and explain the full contents concisely

## -6 created lightweight version of function
created a version of the function that is only for integers to be passed into.