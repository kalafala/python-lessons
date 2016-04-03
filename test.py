#!/usr/bin/python
print ('hello world')

# list all builtin functions
dir(__builtins__)

# various operations on lists
family =['kerim','kristen','alexis','addison']
ages = [41, 39, 10, 7]

print(family)
print(family[0])
print(family[0:2])
print(family[-2])
print(family[-3:]);
print(family[0::2]);

family.append('socks');
print(family);
family.extend(ages);
print(family);

family.remove('socks');
print(family);

print(family,ages);
print(len(family));
print(max(ages))

# Examples with type-casting
val1 = int(input("enter value one: "));
val2 = int(input("enter value two: "));
val3 = int(input("enter value three: "));

maximum = max(val1, val2, val3);

# Illustration of concatination
print("The maximum is " + str(maximum));
