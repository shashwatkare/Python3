"""
This is a simple code to test if any number given as input by user is prime or not.
Prime numbers are only divisible by 1 or by themselves.

I have also introduced one line of code to give exact multiplication of 'not prime' number
"""



num = int(input("Enter a number: "))

if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
   
   
   """
   There is another way to do this, by defining a function - which will give you True - if number is prime,
   Flase - if number is non-prime
   """
   
   def is_prime(a):
    return all(a % i for i in range(2, a))
   
   is_prime(13)
   #True
   
   is_prime(12)
   #False
