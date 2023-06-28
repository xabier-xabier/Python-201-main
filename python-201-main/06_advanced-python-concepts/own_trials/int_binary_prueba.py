# Python3 code to demonstrate
# decimal to binary number conversion
# using format() + list comprehension
 
# initializing number
test_num = 999
 
# printing original number
print ("The original number is : " + str(test_num))
 
# using format() + list comprehension
# decimal to binary number conversion
res = [int(i) for i in list('{0:0b}'.format(test_num))]
 
# printing result
print ("The converted binary list is : " +  str(res))