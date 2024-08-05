#R-1.4.py
#Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the positive integers smaller than n.

def return_positive_integer(n):
   # n = print("ENter a positive Integer")

    sum = 0

    while( n != 0):
        sum = sum + n**2
        n = n - 1

        return sum

print(return_positive_integer(3))