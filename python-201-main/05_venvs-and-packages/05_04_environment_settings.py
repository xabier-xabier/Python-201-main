# Create a virtual environment and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.

import os
 
 #Print all the environment variables
#for k, v in os.environ.items():
    #print(f'{k}={v}')



name="ENVIRONMENT"
name1="SECRET"

print(os.environ.get(name))
print(os.environ.get(name1))
