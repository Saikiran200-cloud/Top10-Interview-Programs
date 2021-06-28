number = int(input("Enter the number to be checked :\n"))
for i in range (2,number):
    if number%i == 0:
        print("Not a prime Number...")
        break
    else:
        print("Prime Number...")    
        break
