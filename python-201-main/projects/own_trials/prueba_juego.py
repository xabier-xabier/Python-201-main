
from random import randint

life=1
s1_options=set()
inventory=set()
room=set()
multiplayer=False
x=randint(1,2)   # this will be used only in case the user reaches room 6
multi_=False
init=False

def remove(item):                   #function to remove items in inventory
    if item in inventory:
        inventory.remove(item)
    else:
        print("i am sorry this item is not in your inventory")

    #return item



intro=input("Welcome to dragon fight game, enter a username please: ")
print("\n")
print("Let`s have fun playing ",intro)

s1_options.add(intro)


print("You are in the starting room, there is a room in the right side and another in front'")
print("\n")
print("Your inventory status: ",inventory)
select=input("You can have a look for items if you want: choose: 'look' , 'right' or 'front': ")


while init==False:
    if select=="look":
        room=set()
        room.add(1)
        init=True
    elif select=="right":
        room=set()
        room.add(2)
        init=True
    elif select=="front":
        room=set()
        room.add(5)
        init=True
    else:
        select=input("please choose: 'look' , 'right' or 'front': ")

while life>0:

    while 1 in room: #cambiar a while 1 in room
        print("There are no oponents in this room")
        print("\n")
        print("Your inventory status: ",inventory)
        select=input("you want to look in this room or go to right or front doors? you can also 'check' your inventory. 'look' , 'right','front' or 'check': ")
        while select=="look" and 1 in room:
            print("I am sorry this is an empty room")
            print("\n")
            select=input("you want to stay or go to right or front doors?. 'look' , 'right' or 'front': ")

        if select=="right" and 1 in room:
            room=set()
            room.add(2)
            break
        
        elif select=="front" and 1 in room:
            room=set()
            room.add(5)
            break

        elif select=="check" and 1 in room:
             print("Your inventory status: ",inventory)
             order=input("do you want to remove an item? choose 'remove' or 'leave' ")
             if order=="remove" and 1 in room:
                 order=input("please write the name of the item you want to remove: ")
                 remove(order)

        else:
            pass

    


    while 2 in room: #cambiar a while 2 in room
        print("There are many snakes is this room.")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("do you want to fight? or go to left or front door? 'fight' , 'left','front' or 'check'")

        if select=="fight" and "boots" in inventory and 2 in room:
            print("Congratulations you are wearing your boots and you didn`t get injured")
            print("\n")
            select=input("do you want to  go to left or front door? 'left' or 'front'")
            if select=="left" and 2 in room:
                room=set()
                room.add(1)
                break
            elif select=="front" and 2 in room:
                room=set()
                room.add(3)
                break

        elif select=="fight" and "boots" not in inventory and 2 in room:
            inventory=set()
            print("you lost all the items in your inventory")
            break

        elif select=="left" and 2 in room:
            room=set()
            room.add(1)
            break

        elif select=="front" and 2 in room:
            room=set()
            room.add(3)
            break

        elif select=="check" and 2 in room:
             print("Your inventory status: ",inventory)
             order=input("do you want to remove an item? choose 'remove' or 'leave' ")
             if order=="remove" and 2 in room:
                 order=input("please write the name of the item you want to remove: ")
                 remove(order) 

        else:
            #select=input("do you want to fight? or go to left or front door? 'fight' , 'left' or 'front'")
            pass


    while 5 in room: #cambiar a while 5 in room
        print("There are no oponents in this room")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("Do you want to have a look or go to right, left or back door? choose 'look', 'right', 'left', 'back' or 'check'")

        if select=="look" and 5 in room:
            print("you found a sword, you will need it to fight dragons")
            print("\n")
            inventory.add("sword")
            select=input("Do you want go to right, left or back door? choose  'right', 'left' or 'back'")
            if select=="right" and 5 in room:
                room=set()
                room.add(4)
                break
            elif select=="left" and 5 in room:
                room=set()
                room.add(6)
                break
            elif select=="back" and 5 in room:
                room=set()
                room.add(1)

            else:
                select=input("Do you want go to right, left or back door? choose  'right', 'left','back' or 'check'")

        elif select=="right" and 5 in room:
            room=set()
            room.add(4)
            break

        elif select=="left" and 5 in room:
            room=set()
            room.add(6)
            break

        elif select=="back" and 5 in room:
            room=set()
            room.add(1)
            break

        elif select=="check" and 5 in room:
            print("Your inventory status: ",inventory)
            order=input("do you want to remove an item? choose 'remove' or 'leave' ")
            if order=="remove" and 5 in room:
                order=input("please write the name of the item you want to remove: ")
                remove(order) 

        else:
            pass


    while 4 in room:
        print("There are no oponents in this room")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("Do you want to have a look or go to right, left door? choose 'look', 'right', 'left' or 'check'")
        if select=="look" and 4 in room:
            inventory.add("shield")
            print("You found a 'shield', useful tool for fighting dragons")

        elif select=="right" and 4 in room:
            room=set()
            room.add(3)
            break

        elif select=="left" and 4 in room:
            room=set()
            room.add(5)
            break

        elif select=="check" and 4 in room:
            print("Your inventory status: ",inventory)
            order=input("do you want to remove an item? choose 'remove' or 'leave' ")
            if order=="remove" and 4 in room:
                order=input("please write the name of the item you want to remove: ")
                remove(order) 

        else:
            pass


    while 3 in room:
        print("There is a dragon in the room")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("do you want to fight or go to the door in the right or the door in the left, choose 'fight', 'right', 'left', 'front' or 'check': '")

        if select=="fight" and 3 in room and "sword" in inventory and "shield" in inventory:
            print("Congratulations!! you beat the dragon and won the game")
            room=set()
            life=0
            break

        elif select=="fight" and 3 in room and "sword"not in inventory and "shield" not in inventory:
            print("You are not wearing enough items to beat the dragon, you need a'shield' and a 'sword'")
            print("\n")
            print("Game over")
            room=set()
            life=0
            break

        elif select=="fight" and 3 in room and "sword"not in inventory:
            print("You are not wearing enough items to beat the dragon, you need a'shield' and a 'sword'")
            print("\n")
            print("Game over")
            room=set()
            life=0
            break

        elif select=="fight" and 3 in room and "shield"not in inventory:
            print("You are not wearing enough items to beat the dragon, you need a'shield' and a 'sword'")
            print("\n")
            print("Game over")
            room=set()
            life=0
            break


        elif select=="right" and 3 in room:
            room=set()
            room.add(8)
            break

        elif select=="left" and 3 in room:
            room=set()
            room.add(4)
            break

        elif select=="up" and 3 in room:
            room=set()
            room.add(2)
            break

        elif select=="check" and 3 in room:
            print("Your inventory status: ",inventory)
            order=input("do you want to remove an item? choose 'remove' or 'leave' ")
            if order=="remove" and 3 in room:
                order=input("please write the name of the item you want to remove: ")
                remove(order)

        else:
            pass

    while 8 in room:
        print("There is no oponent in this room")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("do you want to 'look' around or to go 'left' or 'front' door: choose 'look', 'left', 'front' or 'check' ")

        if select=="look" and 8 in room:
            inventory.add("boots")
            print("You found some 'boots', useful for protection against wild animals")

        elif select=="left" and 8 in room:
            room=set()
            room.add(3)
            break

        elif select=="front" and 8 in room:
            room=set()
            room.add(7)
            break

        elif select=="check" and 8 in room:
            print("Your inventory status: ",inventory)
            order=input("do you want to remove an item? choose 'remove' or 'leave' ")
            if order=="remove" and 8 in room:
                order=input("please write the name of the item you want to remove: ")
                remove(order)

        else:
            pass

    while 7 in room:
        
        print("There is a evil wizard in the room, you can`t beat him by your own")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("do you want to 'fight'  or to go 'left' or 'right' door: choose 'fight', 'left','right' or 'check' ")

        if select=="fight" and multiplayer==True and 7 in room:
            print("Congratulations you beat the evil wizard.")
            print("\n")
            select=input(" do you want to go 'left' or 'right' door: choose 'left' or 'right' ")
            if select=="right" and 7 in room:
                room=set()
                room.add(8)
                break

            elif select=="left" and 7 in room:
                room=set()
                room.add(6)
                break

            else:
                select=input(" do you want to go 'left' or 'right' door: choose 'left' or 'right' ")


            while select!="right" or select!="left":
                select=input(" do you want to go 'left' or 'right' door: choose 'left' or 'right' ")

        elif select=="fight" and multiplayer==False and 7 in room:
            print("The wizard was too strong for you. You couldn`t make it")
            print("\n")
            print("game over")
            room=set()
            life=0
            break

        elif select=="left" and 7 in room:
            room=set()
            room.add(6)
            break
        
        elif select=="right" and 7 in room:
            room=set()
            room.add(8)
            break

        elif select=="check" and 7 in room:
            print("Your inventory status: ",inventory)
            order=input("do you want to remove an item? choose 'remove' or 'leave' ")
            if order=="remove" and 7 in room:
                order=input("please write the name of the item you want to remove: ")
                remove(order)

        else:
            pass

    while 6 in room:

        if x==1 and 6 in room and multi_==False:
            multiplayer=True
            print("congratulations you found a partner who will help you during the game")

        elif x==2 and 6 in room and multi_==False:
            multiplayer=False

        print("There is no oponent in this room")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("You can go to 'right' or 'front' door: choose 'right','front' or 'check'")
        multi_=True

        if select== "right" and 6 in room:
            room=set()
            room.add(5)
            break

        elif select=="front" and 6 in room:
            room=set()
            room.add(7)
            break

        elif select=="check" and 6 in room:
            print("Your inventory status: ",inventory)
            order=input("do you want to remove an item? choose 'remove' or 'leave' ")
            if order=="remove" and 6 in room:
                order=input("please write the name of the item you want to remove: ")
                remove(order)



















