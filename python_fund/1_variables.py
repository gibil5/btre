import lib

# Begin
lib.begin()


"""
Python Fundamentals
Created:	18 oct 2019
Last:		id.
"""




'''
Variables
'''
msg = '1. Variables'
lib.print_msg(msg)



x, y, name, is_cool = (1, 2.5, 'Brad', True)

print(x, y, name, is_cool)


# Check type
print(type(x), type(y), type(name), type(is_cool))


# Casting
x = str(x)
print(type(x))

y = int(y)
print(y)




'''
Strings
'''
#print()
#print('# Strings')
#print(line)
msg = 'Strings'
lib.print_msg(msg)


name = 'Brad'
age = str(37)

print('Hello ' + name + ' and I am ' + age)


# Arguments by position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))


# Arguments by name 
print('My name is {name} and I am {age}'.format(name=name, age=age))


# F-Strings only in 3.6
print(f'My name is {name} and I am {age}')


# Methods
s = 'Hello there world 5 !'

print(s.capitalize())

print(s.upper())

print(s.lower())

print(s.swapcase())


# Length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

#count 
sub = 'h'
print(s.count(sub))


# Other
print()
print(s)

print(s.startswith(sub))

print(s.endswith(sub))

print(s.split())

print(s.find('r'))

print(s.isalnum())

print(s.isalpha())

print(s.isnumeric())



# End
msg = '1. Variables - End'
lib.print_end(msg)
