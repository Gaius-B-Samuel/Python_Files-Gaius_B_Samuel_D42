#Exercise 1
print("Bob")
print("ST1001")
print("bob@gmail.com")

#Exercise 2
print("Bob\nST1001\nbob@gmail.com")

#Exercise 3
a = 14
b = 7
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} / {b} = {a / b}")

#Exercise 4
for i in range(1, 6):
    print(i)

#Exercise 5
print("\"SDK\" stands for \"Software Development Kit\", whereas")
print("\"IDE\" stands for \"Integrated Development Environment\".")

#Exercise 6
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

#Exercise 7
num = 23
textnum = "57"
decimal = 98.3
print(type(num))
print(type(textnum))
print(type(decimal))
total = num + int(textnum) + decimal
print("Sum:", total)
print("Datatype of sum:", type(total))

#Exercise 8
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
total_minutes = days_in_year * hours_in_day * minutes_in_hour
print("This program calculates the total number of minutes in a year.")
print(f"Total minutes in a year: {total_minutes}")

#Exercise 9
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")


