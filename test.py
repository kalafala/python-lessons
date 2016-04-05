#!/usr/bin/python


# Credit:  https://www.youtube.com/watch?v=41qgdwd3zAg&list=PLexnxRP3h0cpct0qgJwvFvnWTuQOTIqh0&index=1
#   And further vidoes in this series

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
print(family[0::2])
print(family[::2])
print(family[::-2])

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

# Note that indentation is important !
if val1>0:
	print ("val1 " + str(val1) + " is greater than zero")
	if val2>0:
		print ("val2 " + str(val2) + " is greater than zero")
	else:
		print ("val2 " + str(val2) + " is less than or equal to zero")
	print ("end of if")
elif val1==0:
	print ("val1 " + str(val1) + " is equal to zero")
	print ("end of elif")
else:
	print ("val1" + str(val1) + " is less than zero")
	print ("end of else")

print ("end of if-elif-else");

count=1
while count<5:
	print(count)
	count+=1

for num in ages:
	print num

# function definition
def mysum (arg1, arg2):
	return arg1+arg2

print ("The sum of " + str(val1) + " and " + str(val2) + " is " + str(mysum(val1,val2)))

def mysum2 (arg1=0,arg2=0):
	return arg1+arg2*arg2


print ("The sum of <default>  and  <default> squared is " + str(mysum2()))
print ("The sum of 2  and  <default> squared is " + str(mysum2(2)))
print ("The sum of <default>  and  2 squared  is " + str(mysum2(arg2=2)))
print ("The sum of 2  and  2 squared  is " + str(mysum2(2,2)))

# Variable argument length
def mysum3(arg1, *arg2):
	sum=arg1
	for num in arg2:
		sum+=num
	return sum

print ("The sum of 1,2,3 is: " + str(mysum3(1,2,3)))

# class definition
# Note that all member functions require at least the "self" argument as the *first* argument

class person:
	def __init__(self, id):
		self.firstName="defaultFirst"
		self.lastName="defaultLast"
		self.id=id;
	def __del__(self):
		self.printMe()
		print(".. is destroyed")
	def setName(self, fName, lName):
		self.firstName=fName
		self.lastName=lName
	def printMe(self):
		print(str(self.id) + " " + self.firstName + " " + self.lastName)

Kerim = person(1)

# Note that the "self" argument is implicit
Kerim.printMe()
Kerim.setName("Kerim", "Kalafala")
Kerim.printMe()

# Destructor gets called automatically when Kerim goes out of scope
