

def inttester(numberinput):
    try:
        # we cast it as an string first, otherwise this operation rounds floats
        numbertotest = int(str(numberinput))
        return numbertotest
    except:
        # check if the number is an exact float ending in .0
        try:
            numbertotest = int(numberinput)
            if numberinput - numbertotest == 0:
                return numbertotest
            else:
                # if not an integer then return a helpful output
                return "error in input, please ensure only a whole number is used"
        except:
            # if not an integer then return a helpful output
            return "error in input, please ensure only a whole number is used"

print(inttester(15.0))
