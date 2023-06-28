# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def advrt(location,budget,garage,garden,train):
    print(f"""                   **New Home for sale in {location}**
                Based on the budget you told us of {budget} we 
                found a good opportunity for you.
                The house has a big {garage} and a 200m2 {garden}.
                
                It is located just 5 min away from the nearest {train}.
                Don`t loose this chance to get the house you have been looking for.""")


info=("Santa Rosa","250.000$","garage","garden","train station")

advrt(*info)