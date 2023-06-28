# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

text=input("Please write a sentence: ")


cut=text.split()
tup=tuple(cut)
long=len(tup)

list_f=[]

for i in range(0,long,1):
    lista=list(tup[i])
    tup_i=tuple(lista)
    list_f.append(tup_i)
   

print(list_f)
















