def my_function(param1='default'):
    """
    This is the docstring
    This comes up when you hover over the function
    """
    print("my first python function {}".format(param1))

my_function()


def hello():
    return "Hello"

greeting = hello()

print(greeting)

def addNum(num1,num2):
    if type(num1)==type(num2)==int:
        return num1+num2
    else:
        return "Sorry, I need integers"

result = addNum(2,2)
print(result)
print(type(result))


# lambda expression - One time use function
# Lambda Expression

# Filter
mylist = [1,2,3,4,5,6,7,8]

# return true if the number is even
def even_bool(num):
    return num%2 == 0

# collect all of the even numbers in a list using the filter function
evens = filter(even_bool,mylist)
# print the even numbers, casted to a list
print(list(evens))

# Above expression as a lambda
evens = filter(lambda num: num%2 == 0,mylist)
print(list(evens))


# useful functions
st = 'hello'
print(st.lower())
print(st.upper())

tweet= "Go Sports! #Sports"
result = tweet.split('#')
print(result)
result = tweet.split('#')[0]
print(result)

# In functions
print('x' in [1,2,3])

