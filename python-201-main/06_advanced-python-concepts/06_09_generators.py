# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.

generator = (x*2 for x in range(5))
print(generator)  # OUTPUT: <generator object <genexpr> at 0x1106845f0>
print(type(generator))  # OUTPUT: <class 'generator'>

for i in generator:
    print(i)


#0
#2
#4
#6
#8