# Write a dictionary comprehension that maps each integer
# between `0` and `999` to a list of the digits that represents
# that integer in base 10. That is, your output should be:
#
# {0: [0], 1: [1], 2: [2], 3: [3], ...,
# 10: [1, 0], 11: [1, 1], 12: [1, 2], ...,
# 999: [9, 9, 9]}
#
# CHALLENGE: Write another dictionary comprehension that works the same
# but for base 2 (binary)! The output values should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1], ...,
# 7: [1, 1, 1], 8: [1, 0, 0, 0], 9: [1, 0, 0, 1], ...,
# 999: [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]}


# base 10 situation
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


final={x*base**2+y*base+z : [x,y,z] for  x in digits  for y in digits for z in digits}

print(final)


# base 2 situation

final1={num :list('{0:0b}'.format(num)) for num in range(0,250,1)}
print(final1)
final1={num :list('{0:0b}'.format(num)) for num in range(251,500,1)}
print(final1)
final1={num :list('{0:0b}'.format(num)) for num in range(501,750,1)}
print(final1)
final1={num :list('{0:0b}'.format(num)) for num in range(751,1000,1)}
print(final1)



