#C-1.21-1

try:
    num = int(input("Enter an Integer number : "))
    print(num * 10)
    
except EOFError as er :
    print(er)
    
    
