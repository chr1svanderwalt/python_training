myUniqueList = []
myLeftovers = []

def add_things(list_item1):

    if list_item1 in myUniqueList:
        myLeftovers.append(list_item1)
        print("False")
        #print(myLeftovers)
    else:
        myUniqueList.append(list_item1)
        print("True")
        #print(myUniqueList)

# Test the list 
add_things("apple")
add_things("orrange")
add_things("melon")
add_things("apple")
add_things(30)
add_things(32)
add_things("Jamie")
add_things("Chris")
add_things("30")
add_things("grapes")
add_things("apple")
add_things("orrange")
add_things("melon")
add_things("apple")
add_things(30)
add_things(32)
add_things("jamie")
add_things("chris")
add_things("30")
add_things("grapes")
add_things("pizza")
add_things("PIZZA")
add_things('pizza')
# Print out the results
print('My unique list')
print(myUniqueList)

# Confirm Reject list works
#print('My leftovers list')
#print(myLeftovers)


         