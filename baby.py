import calendar

year = input("Enter birth year: ")
birth_year = year
age  = 2024 - int(birth_year)
if age >= 18:
    print("Congrats! You are old enough. YOu may enter the party!")
else:
     print("Unfortunately, you are too young")

print()


# def age_calculator(current_year,birth_year):
#    age = current_year - birth_year
#    print("The age of the person in years is",age,"years")
# age_calculator(2023,1995)