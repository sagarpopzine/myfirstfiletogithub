height=int(input("enter your height in feet: "))
bill=0
if height>=3:
    print("you can ride")
    age=int(input("enter your age: "))
    if age<12:
        bill=150
        print("ticket price is 150rs")
    elif age<18:
        bill=250
        print("ticket price is 250rs")
    elif age>=18:
        bill=500
        print("ticket price is 500rs")
    want_photo=input("do you want photo [Y/N]: ")
    if want_photo == "y" or want_photo == "Y":
        bill=bill+50
    print(f"your total bill is {bill}")
else:
    print("you can't ride")   
print("thank you enjoy your ride") 