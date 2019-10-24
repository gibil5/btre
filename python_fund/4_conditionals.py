import lib

# Begin
lib.begin()


'''
Functions
'''
msg = '4. Conditionals'
lib.print_msg(msg)

# Operators
# Comparison
# Logical 
# Membership
# Identity


x = 7
y = 5


# Comparison
if x == y:	
	print(f'{x} is equal to {y}')


if x > y:
	print(f'{x} is greater to {y}')

elif x == y:
	print(f'{x} is equal to {y}')

else:
	print(f'{x} is less to {y}')


# Nested ifs 


# Logical
if x > 5 and x < 10:
	print(f'{x} is greater than 5 and less than 10')
# or
# not


# Membership

numbers = [1, 2, 3, 4, 5, 6, 7]

if x in numbers:
	print(f'{x} is in the list')



# Identity

if x is y:
	print(f'{x} is {y}')

if x is not y:
	print(f'{x} is not {y}')







# End
msg = '4. Conditionals - End'
lib.print_end(msg)


