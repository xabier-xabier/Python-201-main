# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

list=[1,2,6,55,2,"hi",4,6,1,13]

for i in list:
    count_n=list.count(i)
    if count_n!=1:
        for x in range(1,count_n+1,1):
            list.remove(i)



print(list)

