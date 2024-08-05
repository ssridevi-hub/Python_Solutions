def is_even(k):

    invalue = int(k)


    print("\n BAM! %d is Even\n" %invalue if (-1)**invalue == 1  else "No Way! %d is not even \n" %invalue)
    
    print("YEAH, %d  is Even number \n"  %invalue if (-1)**invalue == 1  else "No way! %d is not even \n" %invalue)

is_even(24)