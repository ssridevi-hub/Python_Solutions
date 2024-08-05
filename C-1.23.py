# Give an example of a Python code fragment that attempts to write an element to a list based 
# on an index that may be out of bounds. If that index is out of bounds, the program should catch 
# the exception that results, and print the following error message: “Don’t try buffer overflow attacks in Python!”


data = [8,5,8, 4, 6, 5, 4, 9, 6, 10, 23]

try:
    data[15] = 27
except:
    print('Don’t try buffer overflow attacks in Python!')

