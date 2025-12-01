size=input("enter your pizza size(S/M/L): ")
bill=0
if size == 'S' or size == 's':
    bill += 100
    print("your pizza price is 100rs")
elif size == 'M' or size == 'm':
    bill += 200
    print("your pizza price is 200rs")
elif size == 'L' or size == 'l':
     bill += 300
     print("your pizza price is 300rs")
else:
    print("invalid size entered")
pepperoni=input("do you wnat pepperoni[Y/N]: ")
if pepperoni == 'Y' or 'y':
    if size == 'S' or 's':
        bill += 30
    else:
        bill += 50
else:
    print("invalid entry")
cheese=input("do you want cheese[Y/N]")
if cheese == 'Y' or 'y':
    bill += 20
print(f"your total bill is {bill}")    
