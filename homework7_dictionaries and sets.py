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

# Tuples that is contained in the byob dict.
band_members = ("Serj tankian", "Daron malakian", "Shavo odadjian", "John dolmayan")
producer = ("Rick rubin", "Daron malakian")

# Dict. that contains all song information.
byob = {"Song": "Byob", 
        "Band": "System of a down",
        "Members": band_members,
        "Writer": "Serj tankian", 
        "Producer": producer, 
        "Album": "Mezmarized", 
        "Released": "2005", 
        "Genre": "Metal"
        }

# loop through the dict diplaying each element of the dict 
for x, y in byob.items():
       print(str(x) + ": " + str(y))


# guessing game
print("\nCategories to choose from\n")
for category in byob:
        print(category)

varA = str.capitalize(input("\nChoose a Category: "))
varB = str.capitalize(input("\nGuess the Awnser: "))

def guess(varA, varB):
        while True:
                if varB == byob[varA]:
                        print(True)
                        break
                else:
                        print(False)

guess(varA,varB)
