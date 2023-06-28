# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list=[]


for i in starter_list:
    for y in i:
        flattened_list.append(y)


print(flattened_list)


# Flatten any depth of list

from iteration_utilities import deepflatten   #from  a library in python "iteration_utilities" import "deepflatten"
starter_list1 = [[30,7],[8,9],[30,7],[8,9],[ [200 ] ]]   
print("list starter_list before flattening", starter_list1)
flatten_lst = list(deepflatten(starter_list1))               # add the list as an argument when calling the function "deepflatten"
print("list starter_list after flattening", flatten_lst)

