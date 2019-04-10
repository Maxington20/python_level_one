# Given the string:
s = 'django'

# use indexing to print out the following:
# d, o , djan, ,jan,go

# bonus, use indexing to reverse the string

print(s[0])

print(s[-1])

print(s[:4])

print(s[1:4])

print(s[4:])

# Reverse the string
# beginning to end, step size of -1
print(s[::-1])



# Given this nested list:

l = [3,7,[1,4,'hello']]

# REassign hello to be goodbye

l[2][2] = 'Goodbye'

print(l)


#Problem 3. Using keys and indexing, grab the 'hello' fromt he following dictionaries
d1 = {'simple_key': 'hello'}

d2 = {'k1': {'k2': 'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}


print(d1['simple_key'])

print(d2['k1']['k2'])

# This one was hard, and I coulnd't figure it out without checking the solutions
print(d3['k1'][0]['nest_key'][1][0])



# Use a set to find the unique values of the list below:

mylist = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,3]

mySet = set(mylist)

print(mySet)


# you are given to two variables. put them in this sentence
age = 4
name = "Sammy"
# "hello my dog's name is Sammy and he is 4 years old"
# x = "Item One: {x} Item Two: {y}".format(x="dog",y="cat")
print("Hello my dog's name is {name} and he is {age} years old.".format(name = "Sammy",age = 4))
