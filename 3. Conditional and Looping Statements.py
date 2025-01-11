#Cinema Ticket Price
age=int(input("Enter your age: "))
full_price=6
if age<16:
    price=full_price/2
elif age>=60:
    price=full_price/3
else:
    price=full_price
print(f"Your ticket costs",price)

#Greatest of Three Numbers
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
greatest=max(a,b,c)
print(f"The greatest number is: {greatest}")

#Factorial using Loops
num=int(input("Enter a number: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"The factorial of {num} is {factorial}")

#Reverse a Number
num=int(input("Enter a number: "))
reversed_num=0
while num>0:
    reversed_num=reversed_num*10+num%10
    num=num/10
print(f"Reversed number is: {reversed_num}")

#Multiples of a Number
num=int(input("Enter a number: "))
limit=int(input("Enter the limit for multiples: "))
for i in range(1,limit+1):
    print(f"{num}x{i}={num*i}")

#Loop and Break
while True:
    value=input(":")
    print(value)
    if value.lower()=="done":
        print("Done")
        break

#FizzBuzz
for i in range(1, 11):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#Pattern Printing
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
