import lib

# Begin
lib.begin()



'''
Lists
'''
msg = '2. Lists'
lib.print_msg(msg)

# Create
numbers = [1,2,3,4,5]
print(numbers)
print(type(numbers))


# Using a constructor
numbers = list((1,2,3,4,5))
print(numbers)


# Get value
#fruits = ['Apples', 'Oranges', 'Grapes', 'Pears', 12]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
print(fruits)
print(len(fruits))


# Append
fruits.append('Mangoes')
print(fruits)

fruits.remove('Grapes')


fruits.insert(2, 'Strawberries')
print(fruits)


# Remove from position
fruits.pop(3)
print(fruits)



# Reverse
fruits.reverse()
print(fruits)


# Sort
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)





'''
Tuples and Sets
'''
msg = 'Tuples and Sets'
lib.print_msg(msg)


# Tuple is a collection which is ordered and unchangeable

fruit_tuple = ('Apple', 'Orange', 'Mango')
print(fruit_tuple)


#fruit_tuple[1] = 'Grape'

tuple_2 = ('Apple', )
print(tuple_2)

print(len(tuple_2))

del tuple_2
#print(tuple_2)





# Set is a collection which is unordered and unindexed. No duplicate members. 

#fruit_set = {'Apple', 'Orange', 'Mango'}
fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}
print(fruit_set)

print('Apple' in fruit_set)


fruit_set.add('Grape')
print(fruit_set)

fruit_set.remove('Grape')
print(fruit_set)


fruit_set.clear()
print(fruit_set)

del fruit_set
#print(fruit_set)




'''
Dictionaries
'''
msg = 'Dictionaries'
lib.print_msg(msg)

# A collection which is unordered, changeable and indexed. 
# No duplicate members. 
# Ruby hash
# JSON decoded into a dic

person = {
			'first_name': 'John',
			'last_name': 'Doe',
			'age': 30,
}
print(person)


person = dict(	
			first_name='John',
			last_name='Doe',
			age=30,
)
print(person)


print(person['first_name'])

print(person.get('first_name'))

person['phone'] = '123456'

print(person)

print(person.keys())
print(person.values())
print(person.items())
print()

person2 = person.copy()

person2['city'] = 'Boston'
print(person2)
print()


# Remove
print(person)
del(person['age']) 
person.pop('phone')

print(person)


# Clear
person.clear()
print(person)
print(len(person))
print()



# List of dictionaries
people = [
			{
				'first_name': 'John',
				'last_name': 'Doe',
				'age': 30,
			},

			{
				'first_name': 'Peter',
				'last_name': 'Parker',
				'age': 41,
			},
]
print(people)
print(people[1]['first_name'])




# End
msg = '2. Lists - End'
lib.print_end(msg)
