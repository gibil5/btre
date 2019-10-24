import os 


def begin():
	os.system('clear')  # For Linux/OS X




def print_end(msg):
	print()
	print()
	print()
	print(msg)
	print()


def print_msg(msg):
	
	#line = '-----------------------------------'
	line = '---------------------------------------------------------'

	se = '***\t'

	#line = '###################################'

	print()
	print()
	print(line)
	print(f'{se} {msg}')
	print(line)
	print()
