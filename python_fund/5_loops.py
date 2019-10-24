import lib

# Begin
lib.begin()


'''
Loops
'''
msg = '5. Loops'
lib.print_msg(msg)


# Iterate over a sequence

people = ['John', 'Will', 'Janet', 'Karen', ]



# For Loop

print()
print('For')

# Break
for person in people:
	if person == 'Janet':
		break
	print(person)


print()
# Continue
for person in people:
	if person == 'Janet':
		continue
	print(person)



# Range
print()
print('Range')
for i in range(len(people)):
	print(people[i])


print()
for i in range(0, 10):
	print(i)



# While
print()
print('While')
count = 0
while count <= 10:
	print(count)
	count += 1



# End
msg = 'End'
lib.print_end(msg)
