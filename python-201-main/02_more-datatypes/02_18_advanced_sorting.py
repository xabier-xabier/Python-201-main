# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!


input_dict = {"item1": 5, "item2": 6, "item3": 1}



cont=0
list=[]
list_f=[]


for i in input_dict:
    list.append(i)
    list.append(input_dict[i])

for i in list:
    cont+=1 
    if cont<2:
        tup1=i
    elif cont==2:
        tup2=i
        tup_f=tup1,tup2
        tup=tuple(tup_f)
        list_f.append(tup)
        cont=0

print(list_f)



    

