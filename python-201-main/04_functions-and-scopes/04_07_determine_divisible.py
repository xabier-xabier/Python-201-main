# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages


def or_function(number):
    if number%4==0 and number%7!=0:
        sol4=True
        sol7=False

    elif number%4!=0 and number%7==0:
        sol4=False
        sol7=True
    else:
        sol4=False
        sol7=False

    return [sol4,sol7]

def and_function(number):
    if number%4==0 and number%7==0:
        sol=True
    else:
        sol=False

    return sol


text=int(input("Please write a number between 1 and 1,000,000,000: "))

out_or= or_function(text)
out_and=and_function(text)


if out_and==True:
    print(text, "is divisible by 4 and 7")

elif out_and==False:
    #print(text, "is not divisible by 4 and 7")

    if out_or[0]==True and out_or[1]==False:
        print(text, "is divisible by 4 but not by 7")

    elif out_or[0]==False and out_or[1]==True:
        print(text, "is divisible by 7 but not by 4")

    elif out_or[0]==False and out_or[1]==False:
        print(text, "is not divisible by 7 neither by 4")



