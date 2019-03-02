
def compair(varA, varB, varC):
    if int(varA) == int(varB) or int(varA) == int(varC) or int(varB) == int(varC):
        return True
    else:
        return False


""" Test for function to determin if function work correctly """
print(compair(5,5,7.5))

print(compair(5000,6,5000))

print(compair(5,654,654))

print(compair(1,2,3))
