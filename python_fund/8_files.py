import lib

# Begin
lib.begin()



'''
Files
'''
msg = '8. Files'
lib.print_msg(msg)


# open
my_file = open('my_file.txt', 'w')
print(my_file.name)
print(my_file.closed)
print(my_file.mode)


my_file.write('I love Python')
my_file.write(' and Javascript')

my_file.close()


# Append
my_file = open('my_file.txt', 'a')  		# So that it will not be overriden
my_file.write(' and I also like PHP')
my_file.close()


# Read
my_file = open('my_file.txt', 'r+')
text = my_file.read(10)  	# the first 10 characters
print(text)




# End
msg = 'End'
lib.print_end(msg)
