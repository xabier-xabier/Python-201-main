# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.


s1=set()
long=0
point=5

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")

    return val


while long<10:

    text=input("Please enter a number(integer): ")
    conv=check_user_input(text)

    if type(conv)==int: # True:

        if text not in s1:
            s1.add(text)
            long+=1
        

        elif text in s1:
            print("The number was already in the set")
            point-=1
            print(point, "points remaining")
            if point==0:
                print("Game over")

    else:
        print("That is not a integer")

print("Congratulations you created a 10 item set:")
print(s1)



