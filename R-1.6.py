# R-1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sumOfSquares_odd_positive_integers(n):

    return sum(x**2 for x in range(1,n) if x % 2 == 1)

print(sumOfSquares_odd_positive_integers(5))