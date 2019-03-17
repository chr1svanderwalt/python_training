"""
Homework Assignment #7: Dictionaries and Sets

Details:
Return to your first homework assignments, when you described your favorite song. 
Refactor that code so all the variables are held as dictionary keys and value. 
Then refactor your print statements so that it's a single loop that passes through each item in the dictionary and prints out it's key and then it's value.

Extra Credit:
Create a function that allows someone to guess the value of any key in the dictionary, and find out if they were right or wrong. 
This function should accept two parameters: Key and Value. 
If the key exists in the dictionary and that value is the correct value, then the function should return true. 
In all other cases, it should return false.
"""
# Dict. that contains all song information.
byob = {"Song": "Byob", 
        "Band": "System of a down",
        "Writer": "Serj tankian", 
        "Producer": "Serj tankian", 
        "Album": "Mezmarized", 
        "Released": "2005", 
        "Genre": "Metal"
        }

# loop through the dict diplaying each element of the dict 
for x, y in byob.items():
       print(str(x) + ": " + str(y))

#Guessing Game
print("\nCategories to choose from\n")
for category in byob:
        print(category)

varA = str.capitalize(input("\nChoose a Category: "))
varB = str.capitalize(input("\nGuess the Awnser: "))

def guess(varA,varB):
        while True:
                if varA in byob: #check if the key is in the dict.
                        if varB in byob[varA]: #check if the awnser is correct
                                print(True)
                                break
                        else:
                                print(False)                        
                                varB = str.capitalize(input("\nGuess the Awnser: "))
                else:
                        print(False)
                        varA = str.capitalize(input("\nChoose a Category: "))
                
guess(varA,varB)
