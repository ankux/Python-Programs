import math

while True:
    def factorial(n):
        if n == 0:
            print("\tThe factorial of",n,"is 1")
        else: 
            result = math.factorial(n)
            print("\tThe factorial of",n,"is: ",result)

    n = int(input("\nEnter the number: "))
    factorial(n)
