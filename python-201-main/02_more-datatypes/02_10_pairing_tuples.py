# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

x=randlist
x.sort()

count=0
cont=0
long=len(x)
list=[]
list_t=[]
tup=()

if long%2==0:
    for i in x:
        count+=1
        if count<2:
            list.append(i)

        elif count==2:
            list.append(i)
            a=tuple(list)
            list_t.append(a)
            list=[]
            count=0

elif long%2!=0:
    for i in x:
        cont+=1
        count+=1
        if count<2 and cont!=long:
            list.append(i)

        elif count==2 and cont!=long:
            list.append(i)
            a=tuple(list)
            list_t.append(a)
            list=[]
            count=0
        
        elif cont==long:
             list.append(i)
             b=0
             list.append(b)
             a=tuple(list)
             list_t.append(a)
             list=[]
             count=0

for i in list_t:
    print(i)

    
print(list_t)

