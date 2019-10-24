import lib

# Begin
lib.begin()


'''
Functions
'''
msg = '3. Functions'
lib.print_msg(msg)


# We use indentation and a colon

def sayHello(name='Sam'):
	"""
	Prints Hello and then name.
	"""
	print('Hello ' + name)

sayHello()
sayHello('Beth')



def getSum(n1, n2):
	total = n1 + n2
	return total 

num = getSum(1, 3)
print(num)



def addOneToNum(num):
	num += 1
	return num

num = addOneToNum(6)
print(num)



# Lambda functions 
# lambda function is a small anonymous function
# That can take any number of arguments
# but can only have one expression
# They have to be simple

getSum = lambda num1, num2: num1 + num2
print(getSum(9, 2))

addOneToNum = lambda num: num + 1
print(addOneToNum(5))




# End
msg = '3. Functions - End'
lib.print_end(msg)
