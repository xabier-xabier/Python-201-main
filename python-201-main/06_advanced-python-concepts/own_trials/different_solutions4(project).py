'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]
'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

# loop for each second argument in tuple
for tup in list(unsorted_list):

    current_min = unsorted_list[0][1]
    index = 0

    for i in range(0, len(unsorted_list)):
        if unsorted_list[i][1] < current_min:   #compare to check if it`s lower than current min`
            current_min = unsorted_list[i][1]
            index = i                           #index stores the position of that min to be added to sorted list and removed from unsorted_list later
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index])

print(unsorted_list)  #Empty list, why print it? to be sure it took all items?
print(sorted_list)