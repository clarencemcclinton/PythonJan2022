weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation

capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

capitals['svk'] = "Habadashary"

# print(weekend["Sat"])
# print(capitals["svk"])

context = {
    'questions': [
        { 
            'id': 1, 
            'content': 'Why is there a light in the fridge and not in the freezer?'
        },
        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
}

# print(context['questions'][2]['content'])

# x = 7
# if (x > 10) and (x < 12):
#     print("it's greater than 10!")
# elif (x > 5):
#     print("it's greater than 5!")
# else:
#     print("number is too low!")

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

def counting_dojo():
# for(var i = 0 ; i < 101 ; i ++)
    for i in range(1, 101, 1):
        # if divisible by 5 print Coding
        if (i % 10 == 0):
            print("Coding Dojo")
        # if divisible by 10 print Coding Dojo
        elif (i % 5 == 0):
            print("Coding")
        else:
            print(i)

# counting_dojo()

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.



# Print the names of your friends with the names of their pets!!
# Print the pets with their types only
friends = [
    {
        "first_name": "Bobothy", 
        "last_name": "Jones", 
        "pets" : 
            [
                {
                    "name": "Squigs",
                    "type" : "turtle"
                },
                {
                    "name": "Spike",
                    "type" : "dog"
                }
            ]
    },
    {
        "first_name": "Sbeve", 
        "last_name": "Tyler", 
        "pets" : 
            [
                {
                    "name": "Sqwuak",
                    "type" : "parrot"
                },
                {
                    "name": "Leo",
                    "type" : "cat"
                },
                {
                    "name": "FeeFee",
                    "type" : "cat"
                }
            ]
    }
]

def print_friend_info(dir):
    new_str = ""
    
    for i in range(0, len(dir), 1):
        # print(dir[i]['first_name'])
        new_str += dir[i]['first_name'] + " - "
        for j in range(0, len(dir[i]['pets']), 1):
            for key, val in dir[i]['pets'][j].items():
                new_str += f"{key} : {val}, "
    return new_str

print(print_friend_info(friends))