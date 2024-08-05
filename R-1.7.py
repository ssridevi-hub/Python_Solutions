# R-1.7.py R-1.7 Give a single command that computes the sum from Exercise R-1.6, 
# relying on Python’s comprehension syntax and the built-in sum function.

n = 7

print(sum(X**2 for X in range(1,n) if X % 2 == 1))