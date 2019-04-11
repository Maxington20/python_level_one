
# Create a function that will return true if the sequence of numbers, 1,2,3 appear in the list somehwere

def array_check(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False




# Given a string, return a new string made of every other character starting with the first, so Hello yeilds HLo
def string_bits(string):
    return string[::2]


x = string_bits("HeeoLoLeo")
print(x)


# Given two strings, return true is either of the strings appears at the very end of the other string, ignoring upper/lower
# case differences.

def end_other(a,b):
   a = a.lower()
   b = b.lower()

    # better way to do this
   return (b.endswith(a) or a.endswith(b))

    # This is stupid, will use the thing above if i ever need this kind of functionality again
   # return a[-(len(b)):] == b or a == b[-len(a):]
    


# Given a string, return a string where for every char in the original, there are two chars

def double_char(string):
    result = ""
    for char in string:
        result =+ char*2
    return result


# Given 3 int values, abc, return their sum. However, if any of the values is a teen, 13-19 inclusive, then that value counts as
# 0, except 15 and 16 do not count as a teen. Write a separate helper "def fix_teen(n):"" that takes in an int value and returns that value
# for the teen rule

# In this way, you avoid repeating the teen code 3 times (i.e. decomposition)
# Define the helper below and at the same indent level as the main no_teen_sum(). Again you will have two functions for this problem


# def no_teen_sum(a,b,c):
#     if a in range(13,20):
#         fix_teen(a)
#     if b in range(13,20):
#         fix_teen(b)
#     if c in range(13,20):
#         fix_teen(c)
#     return a + b + c

# def fix_teen(n):
#     if n != 15 and n != 16:
#         n = 0
#         return n

def no_teen_sum(a,b,c):
    return int(fix_teen(a)) + int(fix_teen(b)) + int(fix_teen(c))

def fix_teen(n):
    if n in [13,14,17,18,19]:
        return 0
    return n


x = no_teen_sum(19,2,3)
print(x)


# Return the number of even integers in the given array
def count_evens(nums):
    count = 0
    for num in nums:
        if num %2 == 0:
            count +=1
    return count

x = count_evens([1,2,3,4,5,6])
print(x)