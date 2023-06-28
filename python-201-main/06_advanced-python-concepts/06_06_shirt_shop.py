# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

list_comp=[(i,j) for i in colors for j in sizes ]

print("the cartesian product is: ",str(list_comp))