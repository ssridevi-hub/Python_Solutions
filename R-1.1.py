#print("HelloWOrld!!!")

def is_multiple(n,m):

    try:
        if m%n == 0:
            print("Yes, {0} is a factor of {1}".format(n,m) )
        else:
            print("\n Nope! {0} is not a factor of {1}".format(n,m))
    except Exception as excpt:
        print("Error!", excpt)
    
is_multiple(3,15)
