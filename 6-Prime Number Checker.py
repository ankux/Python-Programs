n = int(input("Enter the Number to check if its a Prime Number: "))

if n>1:
    for i in range(2,n):
        if (n%i) == 0:
            print("Nope!",n,"is not a Prime Number!")
            break
    else:
        print("Yes",n,"is a Prime Number!")