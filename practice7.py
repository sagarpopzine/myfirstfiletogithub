age=int(input("enter your age: "))
years_left=100-age
days_left=years_left*365
weeks_left=years_left*52
months_left=years_left*12
hours_left=years_left*8760
print(f"you have {days_left} days, {weeks_left} weeks, {months_left} months, {hours_left} hours left")