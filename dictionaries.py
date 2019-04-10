my_stuff = {"key1":"value","key2":"value2"}

print(my_stuff['key1'])

my_stuff = {"key1":123,"key2":"value2","key3":{'123':[1,2,'grabme']}}

# should print grabme
print(my_stuff['key3']['123'][2].upper())

my_stuff = {'lunch':'pizza', 'bfast':'eggs'}

my_stuff['lunch']= 'burger'

my_stuff['dinner']='pasta'

print(my_stuff['lunch'])
print(my_stuff)
