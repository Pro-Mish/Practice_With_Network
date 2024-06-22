import calendar

year = input("Enter birth year: ")
birth_year = year
age  = 2024 - int(birth_year)
if age >= 18:
    print("Congrats! You are old enough. YOu may enter the party!")
else:
     print("Unfortunately, you are too young")
