# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# method 1 change to set

set_1=set(list_)

print(set_1)

# method 2

for i in list_:
    count_n=list_.count(i)
    while count_n!=1:
        list_.remove(i)
        count_n=list_.count(i)


print(list_)
