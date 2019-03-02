""" 3 functions to display info based on Homework assignment 1"""
def band():
    print("System of a Down")

def year():
    print("March 29, 2005")
 
def genre():
    print("Nu Metal, Trash Metal")

""" a fun function to ask for user input based in the 3 functions band, year and genre """
def info():
    # answer check to prevent an infinite loop
    ans_check = False
    # loop until the user supplies a valid answer
    while ans_check == False:
        user_input = input('Choose one of the following options\n 1. Artist\n 2. Year\n 3. Genre\n')
    # if statement to check the user input and print out the results    
        if user_input == '1':
            band()
            ans_check = True
        elif user_input == '2':
            year()
            ans_check = True
        elif user_input == '3':
            genre()
            ans_check = True
        else:
            print("Incorrect input please press 1, 2, or 3")

# calls the info function.
info()


