'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]
'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

# take the second argument "4" , "2" and "6"
for x in range(0, len(unsorted_list)):

    min = unsorted_list[0][1]
    print(min)
    index = 0

# compare that second argument in another loop with the rest of the other arguments "2","4","6"
    for i in range(0, len(unsorted_list)):
        if unsorted_list[i][1] < min:
            min = unsorted_list[i][1]
            index = i
    sorted_list.append(unsorted_list[index])                  #if it`s smaller adds it`
    unsorted_list.remove(unsorted_list[index])                # removes that tuple


print(unsorted_list)                #doesn`t make any sens to print this, it`s empty
print(sorted_list)