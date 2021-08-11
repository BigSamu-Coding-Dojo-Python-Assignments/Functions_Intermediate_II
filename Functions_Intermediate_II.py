#-----------------------------------------------------------------------------------------------
# Excercise_1

# Given the following dictionaries and lists:

x = [ [5,2,3], [10,8,9] ] 
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
print(x) # should pirnt [[5,2,3],[15,8,9]]

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = "Bryant"
print(f"The last name of the first student in the dictionary is {students[0]['last_name']}" ) # should print Bryant as last name

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = "Andres"
print(f"The name of the first scoocer player is {sports_directory['soccer'][0]}") # should print Andres as last name

# Change the value 20 in z to 30
z[0]['y'] = 30
print(f"The new value  of 'y' coordinate in Z is {z[0]['y']}") # should print Andres as last name

#-----------------------------------------------------------------------------------------------

# Excercise_2

# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

def iterateDictionary(studentList):
    for studentDict in studentList:
        completeName =''
        for studentKey in studentDict:
            completeName += f"{studentKey} - {studentDict[studentKey]}, " 
        print(completeName[:-2]) #erasing a comma and space that left. Using slicing method for strings in Python

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel
iterateDictionary(students) 
#-----------------------------------------------------------------------------------------------

# Excercise_3

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

def iterateDictionary_2(keyName, studentList):
    
    if keyName == "first_name" or keyName == "last_name":
        for student in studentList:
            print(f"{student[keyName]}")
    else:
        print("Please provide a correct keyname ('first_name' or 'last_name') and student list")

iterateDictionary_2('first_name', students) # should return Michael, John, Mark, KB
iterateDictionary_2('last_name', students)# should return Jordan, Rosales, Guillen, Tonel

#-----------------------------------------------------------------------------------------------

# Excercise_4
# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# The output should be: 

# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def printInfo(someDictionary):
    for key in someDictionary.keys():
        elementsInKey = len(someDictionary[key])
        print(f"{elementsInKey} {key.upper()}")
        for values in someDictionary[key]:
            print(f"{values}")

printInfo(dojo)