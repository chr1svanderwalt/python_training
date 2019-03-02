""" FizzBuzz Chanllenge with Prime numbers"""

"""Biggest challenge is/was to figure out how to determin prime"""

""" A function to test if a positive integer is prime or not"""
def prime(num):
    if num > 1:
        for i in range(2, num):
            if i % num == 0:
                break
            else:
                print(str(num) + " Prime")
                #print("Prime")
                break

def FizzBuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        #else:
        #    prime(num)

FizzBuzz()
