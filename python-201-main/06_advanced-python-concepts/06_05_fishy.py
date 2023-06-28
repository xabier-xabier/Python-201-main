# Using a listcomp, create a list from the following tuple that includes
# only words ending with -fish. Tip: Use an `if` statement in the listcomp.

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

listcomp=[i for i in fish_tuple if i[-1]=="h" and i[-2]=="s" and i[-3]=="i" and i[-4]=="f"]

print(listcomp)