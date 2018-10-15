N = int(input())
if N % 2 != 0:
    print ("Weird")
else:
    if N >= 2 and N <= 5:
        print ("Not Weird")
    elif N >= 6 and N <= 20:
        print ("Weird")
    elif N > 20:
        print ("Not Weird")
        
#OTHER WAY OF DOING IT        

N = int(input())
if N % 2 != 0:
    print ('Weird')
elif N % 2 == 0 and N == range(2, 5, 1):
    print ('Not Weird')
elif N % 2 == 0 and N == range(6, 20, 1):
    print ('Weird')
elif N % 2 == 0 and N >= 20:
    print ('Not Weird')
else:
    print ('Number out of scope')
    
    
#Note that there are many other solutions and maybe my solutions can be wrong,
#just try to fix and report to me if you find more ways by commenting.
    


