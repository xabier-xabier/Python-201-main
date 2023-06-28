
#base 10
alphabet =  range(10)
base = 10
print(dict((x*base**2+y*base+z,(x,y,z)) for x in alphabet 
                                  for y in alphabet 
                                  for z in alphabet ))


#base 2
alphabet =  range(2)
base = 2
print(dict((x*base**2+y*base+z,(x,y,z)) for x in alphabet 
                                  for y in alphabet 
                                  for z in alphabet ))