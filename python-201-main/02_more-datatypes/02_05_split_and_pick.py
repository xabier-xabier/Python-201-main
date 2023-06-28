# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

text=input("Please write a sentence: ")


a=text.split()
long=len(a)

list=[]

for i in range(0,long,1):
    b=str(a[i])
    l=len(b)
    for j in range(0,l,1):
        list.append(b[j])

max=0
word=None

for i in list:
    calc=list.count(i)
    if calc>max:
        max=calc
        word=i

    elif calc==max:
        word+=i

final_word=set(word)

print("the most common word is: ",final_word)













