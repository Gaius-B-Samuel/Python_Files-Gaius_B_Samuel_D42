#Function with Arguments
def custom_function(arg1,arg2=10,arg3=None):
    if arg3 is None:
        print(arg1+arg2)
    else:
        print(arg1*arg2*arg3)
custom_function(5)
custom_function(5, 20)
custom_function(5, 20, 3)

#Filtering Strings based on length
def filter_strings(strings):
    return [i for i in strings if len(i)>=5]
strings=["apple","dog","banana","cat","grape"]
result=filter_strings(strings)
print(result)

#Evaluate Mathematical Expression
expression="3*5+2"
result=eval(expression)
print(result)

#Filter Prime Numbers
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
numbers=[2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers=list(filter(is_prime,numbers))
print(prime_numbers)

#Convert Strings to Uppercase
strings=["apple","dog","banana","cat","grape"]
uppercase_strings=list(map(str.upper,strings))
print(uppercase_strings)
