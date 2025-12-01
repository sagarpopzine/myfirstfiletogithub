import random
# names=input("enter everybodys name seperated by comma: ")
# name_splits=names.split(",")
# length=len(name_splits)
# random_choice=random.randint(0,length-1)
# print(f"{name_splits[random_choice]} will pay the bill")

names=input("enter everybodys name seperated by comma: ")
name_splits=names.split(",")
random_choice=random.choice(name_splits)
print(f"{random_choice} will pay the bill")
