if 1 < 2:
    print('first block')
    if 20 < 3:
        print('second block')


if 1 > 2:
    print('Hello')
else:
    print('last')


if 1 < -1:
    print('fart')
elif 1 > -1:
    print('burp')


# Loops

# for loops
seq = [1,2,3,4,5,6]

for item in seq:
    print(item)


dic = {"Same":1,"Frank":2,"Dan":3}

for item in dic:
    print(item)

for k in dic:
    print(k)
    print(dic[k])





mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)

# tuple unpacking
for (tup1,tup2) in mypairs:
    print(tup1)
    print(tup2)

# or
for tup1,tup2 in mypairs:
    print(tup1)
    print(tup2)



# While Loops

i = 1
while i < 5:
    print("i is : {}".format(i))
    i += 1


# Range
# range. start, end(not include, step)
print(list(range(0,20,2)))


for item in range(10):
    print(item)


# List comprehension
x = [1,2,3,4]

out = [num**2 for num in x]
print(out)