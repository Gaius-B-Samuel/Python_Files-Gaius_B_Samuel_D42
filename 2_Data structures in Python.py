#List
random_list = [12, 45, 67, 89, 34]
print("Original List:", random_list)
random_list = [12, 45, 67, 89, 34]
print("Original List:", random_list)
for num in random_list:
    print(num)

#Dictionary
my_dict = {'name': 'John', 'age': 25, 'address': 'New York'}
print("Original Dictionary:", my_dict)
my_dict['phone'] = '1234567890'
print("Updated Dictionary:", my_dict)

#Set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)
my_set.add(6)
print("Set After Adding 6:", my_set)
my_set.remove(3)
print("Set After Removing 3:", my_set)

#Tuple
my_tuple = (1, 2, 3, 4)
print("Tuple:", my_tuple)
print("Length of Tuple:", len(my_tuple))