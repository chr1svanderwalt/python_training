"""
Function with Nested Loops and if statements to print a playing board based on screen size.
"""

"""
+1234
0 | | 
1-----
2 | | 
3-----
4 | |

"""

def grid(row, column):
    # Row
    for r in range(row):
        if r % 2 == 0:
            # Column
            for c in range(1, column):
                if c % 2 == 1:
                    if c != column:
                        print(" ", end='')
                    else: # Note # entering this portion of the if statement.
                        print(' ')
                        print(c)
                else:
                    print('|', end='')
        else:
            print('-' * column)

grid(10, 10)
