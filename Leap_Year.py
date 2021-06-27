year = int(input("Enter Year :\n"))
if year%400 == 0:
    print("Leap Year")
elif year%4 == 0:
    print("Leap Year") 
elif year%100 == 0:
    print("Not a leap Year ") 
else:
    print("Not a Leap Year ")          