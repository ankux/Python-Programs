def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
n = int(input("Enter the number: "))
result = factorial(n)
print("The factorial of",n,"is:",result)




'''
eg. factorial of 4 = ?
ans.  4 x factorial(4-1) = 4 x factorial(3)
      factorial(3) = 3 x factorial(2)
      factorial(2) = 2 x factorial(1)
      factorial(1) = 1 x factorial(0)  
      factorial(0) = 1 (as we have already defined in inside the "if-condsition")

      likewise... all the values will be known and finially.. 4 x factorial(3) will be executed! 
'''