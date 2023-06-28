# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(lista:list)->list: # add your arguments
      # add your code implementation
      list=[]
      count=0
      list_f=[]

      for i in lista:
            list.append(count)
            list.append(i)
            tup=tuple(list)
            #print(tup)             You can print it per line
            list_f.append(tup)
            list=[]
            count+=1

      return list_f


courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']

print(my_enumerate(courses))