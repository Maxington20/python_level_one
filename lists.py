mylist = [1,2,3]

mylist = ['string',1,2,3,3.6,'asdf',[1,2,3]]

print(mylist)
print(len(mylist))
print(mylist[0])

# Lists are mutable
mylist[0] = 'New Item'

print(mylist)

mylist.append('New Item')
print(mylist)

mylist.extend(['x','x'])
print(mylist)

item = mylist.pop()
print(mylist)
print(item)

item = mylist.pop(0)
print(item)

mylist.reverse()
print(mylist)

nested_list = [1,2,['x','y','z']]

print(nested_list[2][1])

# List comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]

# the first row of the list 1,4,7
first_col = [row[0] for row in matrix]

print(first_col)