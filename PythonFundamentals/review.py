# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

low = 2
high = 9
mult = 3

for i in range(low, high+1, 1):
    # print(i)
    if i % mult == 0:
        print(i)

# for i in range(5000, -1, -50): 
#     print(i)

# =================================================================

# Values Greater than Second - 
# Write a function that accepts a list 
# and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the input list has less than 2 elements, have the function return False

#     Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#     Example: values_greater_than_second([3]) should return False

# def this_is_the_signature(x, y, z):

def greater_than_second(lst):
    # edge case: if list is too short
    if len(lst) < 2:
        return False
    # create a new list to contain output
    newList = []
    # check original list for what numbers are greater than the 2nd val in the original list
    # for val in range(0, len(lst), 1):
    #     print(lst[val])
    # print("===================")
    for val in lst:
        # print(val)
        if val > lst[1]:
            newList.append(val)
    # print number of values in new list
    print(len(newList))
    # return new list
    return newList

# print(greater_than_second([5,2,3,2,1,4]))
# print(greater_than_second([3]))

# ========================================================================

x = [ 
        [5,2,3], 
        [10,8,9] 
] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

# ========================================================================

# This Length, That Value - 
# Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list 
# whose length is equal to the given size, and whose values are all the given value.

#     Example: length_and_value(4,7) should return [7,7,7,7]
#     Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def this_length_that_value(size, value):
    # create a list
    newList = []
    # make a list length up to the given size
    for x in range(0, size, 1):
        newList.append(value)

    # return the new list
    return newList

print(this_length_that_value(4,7))
print(this_length_that_value(6,2))
