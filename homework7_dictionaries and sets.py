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
"""
|-----
|Notes
|-----
| -Figure out how to make a dictonary gloabl in a function
| -Extra Credit need to be completed
"""

# Tuples that is contained in the byob dict.
band_members = ("Serj Tankian", "Daron Malakian", "Shavo Odadjian", "John Dolmayan")
producer = ("Rick Rubin", "Daron Malakian")
genre = ("Nu Metal", "Trash Metal")

# Track Lenght Variables
lengte_min = 4
lengte_sec = 15
total_seconds = lengte_min * 60 + lengte_sec

# Dict. that containts all song information.
byob = {"Song": "B.Y.O.B", 
        "Band Memenbers": band_members, 
        "Song Writer": "Serj Tankian", 
        "Producer": producer, 
        "Album":"Mezmarized", 
        "Released": "March 29, 2005", 
        "Genre": genre, 
        "Track Lenght": total_seconds}

# loop through the dict diplaying each elemetnt of the dict   
def favSong():    
        for x, y in byob.items():
                print(str(x) + ": " + str(y))
favSong()


"""
Extra Credit
"""
"""
varA = input("1. Guess the category of the a song:\n")
varB = input("2. Guess the value of the category\n")

def guessGame(key, value):


guessGame(varA , varB)
"""
