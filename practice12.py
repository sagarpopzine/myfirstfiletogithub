age=int(input("enter your age: "))
if age >= 18:
    print("eligible to ride")
    signal=input("enter the colour (red, yellow, green): ")
    if signal == "red":
        print("stop for few seconds")
    elif signal == "yellow":
        print("get ready to ride")
    elif signal == "green":        
        print("start the ride")
    else:
        print("you have entered wrong colour ")
else:
    print("not eligible for ride")

