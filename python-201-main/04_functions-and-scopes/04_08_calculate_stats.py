# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(lista):
  # define the function here

  #Find the maximum value
  max_cont=0
  min_cont=lista[0]
  for i in lista:
    if i>=max_cont:
      max_cont=i
    else:
      pass

# find the minimum value
  for j in lista:
    if j<=min_cont:
      min_cont=j
    else:
      pass

# total summation
  sum=0
  for w in lista:
    sum+=w

# Average value
  ave=sum/len(lista)

  print(f"The maximum number is: {max_cont}")
  print(f"The minimum number is: {min_cont}")
  print(f"The summation is: {sum}")
  print(f"The average value is: {ave}")
  pass

# call the function below here

stats(example_list)