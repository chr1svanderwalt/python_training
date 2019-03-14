"""
Function with Nested Loops and if statements to print a playing board based on screen size.

Maximum screen size is 28 x 118 caracters in the defualt command line windows of windows 10
"""

def grid(row,column):
    #check to determin if grid is within size
    if row > 28 or column > 118:
        print(False)
    else:
        # loop to determin the row and what to print in the row
        for r in range(row):
            if r % 2 == 0:
                #loop to determin what to print in the column number position
                for c in range(column):
                    if c % 2 == 0:
                        print(' ', end='')
                    elif c % 2 == 1:
                        print('|', end='')   
            else:
                print('\n' + '-'*column)
        print(True)

grid(6, 10)
