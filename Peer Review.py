#A program that pairs an each student with another student's assignment for review.

'''
Steps
*Assume that the list of names provided is not empty & contains only string
*Define a function to pair students with research work
*create a variable to store the length of the list
*Pair each students's work with the previous student name starting from the second item in the list
*Pair the last research work with the first name in the list
*Return 

'''


def pair_students(names):

    if type(names) != list:
        return'Enter students names in a list'
        

    print('This program pairs a student with another student to peer review their work. \nStudents can find their reviewers below:\n')
    
    n = len(names)
    for i in range (1,n):
        print(names[i] + ' reviews:  ' + names[i-1])

    return (names[0] + ' reviews:  ' + names[n-1])
    


names = ['Ken', 'Stan', 'Pete', 'Pam', 'Rick', 'Morty']
pairing = pair_students(names)
print(pairing)

