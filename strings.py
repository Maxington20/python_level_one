mystring = 'abcdefg'

print(mystring)
print(mystring[0])
print(mystring[2:])
print(mystring[:2]) # up to, but not including index 2
print(mystring[2:5]) # from index to to index 4
print(mystring[::2]) # every other index

# strings are immutable

# string methods
x = mystring.upper()
print(x)

x = mystring.capitalize()
print(x)

mystring = 'Hello World'

x = mystring.split()
print(x)

X = "Inser another string here: {}".format("INSERT ME!")
print(X)

x = "Item One: {} Item Two {}".format("dog","cat")
print(x)

x = "Item One: {x} Item Two: {y}".format(x="dog",y="cat")
print(x)