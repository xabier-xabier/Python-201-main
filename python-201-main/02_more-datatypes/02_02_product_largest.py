# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

list=[]

for i in range(1,6,1):
    text=int(input("Please enter a number: "))
    list.append(text)

list.sort()
print(list[-1])



