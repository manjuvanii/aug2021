def yearcal(age):
    year = str((2021 - age)+100)

    return year

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
print(name + " will be 100 years old in the year", yearcal(age))