# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.



def make_sandwich(bread,*args):
    text=[]
    text.append(bread)
    print(bread)
    #my_list = []
    for i in args:
        text.append(i)
        print(i)
    text.append(bread)
    print(bread)
    change=str(text)
    return change

bread="white bread"
toppings=("tomato","ham","onion","tuna")


sandwich=make_sandwich(bread,*toppings)
print(type(sandwich))
