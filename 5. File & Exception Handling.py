# Exercise 1: Read a file and display its contents
file1=open("file1.txt",'r')
print(file1.read())

# Exercise 2: Copy contents of one file to another file
file1=open("file1.txt",'r')
content=file1.read()
file1.close
file2=open("file2.txt",'w')
file2.write(content)
file2.close()
print("Content copied successfully to a new file.")

# Exercise 3: Count the total number of words in a file
file3=open("file1.txt",'r')
content=file3.read()
words=content.split()
print("Total number of words: ",len(words))

# Exercise 4: Convert string input to integer with exception handling
userinput=input("Enter a string: ")
try:
    number=int(userinput)
    print("Converted Integer:",number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# Exercise 5: Raise an exception if any integer in the list is negative
try:
    numbers=input("Enter a list of integers separated by space: ").split()
    numbers=[int(num) for num in numbers]
    for num in numbers:
        if num<0:
            raise ValueError("Negative number found:",num)
    print("All numbers are non-negative.")
except ValueError as e:
    print(e)

# Exercise 6: Compute the average of a list of integers with exception handling
try:
    numbers=input("Enter a list of integers separated by space: ").split()
    numbers=[int(num) for num in numbers]
    average=sum(numbers)/len(numbers)
    print("Average:",average)
except ValueError:
    print("Invalid input. Please enter integers only.")
except ZeroDivisionError:
    print("Cannot compute average of an empty list.")
finally:
    print("Program finished running.")

# Exercise 7: Write a string to a file with exception handling
try:
    filename=input("Enter the filename: ")
    content=input("Enter the string to write to the file: ")
    with open(filename,'w') as file:
        file.write(content)
    print("Welcome! The string was written to the file successfully.")
except Exception as e:
    print("An error occurred:",e)
