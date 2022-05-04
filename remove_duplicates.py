# Python remove Duplicates from a List
# Method 1
from collections import OrderedDict

my_list = [1, 2, 3, 1, 2, 4, 5, 4, 6, 2]
print("List Before:", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list
print("List After removing duplicates:", my_list)

# Method 2

my_list = ['a', 'x', 'a', 'y', 'a', 'b', 'b', 'c']
my_final_list = OrderedDict.fromkeys(my_list)
print("List After removing duplicates:", list(my_final_list))

# Remove all duplicates from a given string in Python

string = "abxabaxyy"
remove_duplicate = "".join(OrderedDict.fromkeys(string))
print(remove_duplicate)

new_str = ''
for i in string:
    if i in new_str:
        continue
    else:
        new_str = new_str + i

print(new_str)
