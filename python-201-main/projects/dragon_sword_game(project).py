
from random import randint
from pathlib import Path
import csv
import requests

life=1
game_set=set()
s1_options=set()
inventory=set()
room=set()
multiplayer=False
x=randint(1,2)   # this will be used only in case the user reaches room 6
multi_=False
init=False
end_session=False
data_path=Path("/Users/sagar/OneDrive/Escritorio")
cloud=False

# function to remove items from inventory(sword, shield or boots)
def remove(item): 
    '''This function will allow the user
      to remove items from the inventory'''              
    if item in inventory:
        inventory.remove(item)
    else:
        print("i am sorry this item is not in your inventory")

    #return item

# function to write a csv file with the data of the session, all inventory, room when the player end the session, 
# username and game name
def end_ses(count):
    """This function saves csv file of 
    inventory, room, and username"""
    with open(data_path.joinpath("inventory.csv"), "w") as csvfile:
        countwriter = csv.writer(csvfile)
        header=["room","sword","shield","boots","username","game name"]
        data = [count["room"], count["sword"], count["shield"], count["boots"],count["username"],count["game name"]]
        countwriter.writerow(header)
        countwriter.writerow(data)

    pass

# Function to find new name based on the input of the player through API
def call_name(name):
    min=4
    max=len(name)
    URL = f"https://uzby.com/api.php?min={min}&max={max}"
    response = requests.get(URL)

    return response.text

# API to check weather conditions if weather is cloudy depending on the location of the user
def weather(lat,lon):
    API_key="ab429330748f508db5b61e5e5e22dfd1"
    base_url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    response = requests.get(base_url)
    resp_lan=response.json()
    if resp_lan["weather"][0]["main"]=="Clouds":
        cloud=True
    else:
        cloud=False
    return cloud


intro=input("Welcome to dragon fight game, enter a username between 4 and 12 characters please: ")

text_in=False
while text_in==False:
    if len(intro)>=4 and len(intro)<=12:
        game_name=call_name(intro)
        print(f"Your game name is: {game_name}")
        text_in=True

    else:
        intro=input("Please choose a name between 4 and 12 characters: ")

print("\n")
print("Let`s have fun playing ",game_name)

s1_options.add(intro)
game_set.add(game_name)

latitude=float(input("please write the latitude of your location(you can check it in google maps): "))
longitude=float(input("please write the latitude of your location(you can check it in google maps): "))

cloud=weather(latitude,longitude)

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

while life>0 or end_session==False:

    while 1 in room: #Now rooms will be referenced by numbers
        print("There are no oponents in this room")
        print("\n")
        print("Your inventory status: ",inventory)
        select=input("you want to look in this room or go to right or front doors? you can also 'check' your inventory. 'look' , 'right','front','check' or 'end' (end session): ")
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

        elif select=='end' and 1 in room:
            count = {"room": room, "sword": "sword" in inventory, "shield": "shield" in inventory, "boots": "boots" in inventory, "username":s1_options, "game name":game_set}

            end_ses(count)
            print("You eneded the session, your data was saved")
            room=set()
            life=0
            break

        else:
            pass

    
    while 2 in room: #Entering room 2
        print("There are many snakes is this room.")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("do you want to fight? or go to left or front door? 'fight' , 'left','front', 'check' or 'end' (end session)")

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

        elif select=="end" and 2 in room:
            count = {"room": room, "sword": "sword" in inventory, "shield": "shield" in inventory, "boots": "boots" in inventory, "username":s1_options, "game name":game_set}

            end_ses(count)
            print("You eneded the session, your data was saved")
            room=set()
            life=0
            break

        else:
            #select=input("do you want to fight? or go to left or front door? 'fight' , 'left' or 'front'")
            pass


    while 5 in room: #Entering room 5
        print("There are no oponents in this room")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("Do you want to have a look or go to right, left or back door? choose 'look', 'right', 'left', 'back','check' or 'end' (end session)")

        if select=="look" and 5 in room and cloud==False:
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

        elif select=="look" and 5 in room and cloud==True:
            print("It`s very cloudy and the place looks empty")
            print("\n")
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

        elif select=="end" and 5 in room:
            count = {"room": room, "sword": "sword" in inventory, "shield": "shield" in inventory, "boots": "boots" in inventory, "username":s1_options, "game name":game_set}

            end_ses(count)
            print("You eneded the session, your data was saved")
            room=set()
            life=0
            break

        else:
            pass


    while 4 in room:  #Entering room 4
        print("There are no oponents in this room")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("Do you want to have a look or go to right, left door? choose 'look', 'right', 'left','check' or 'end' (end session)")
        if select=="look" and 4 in room and cloud==False:
            inventory.add("shield")
            print("You found a 'shield', useful tool for fighting dragons")

        elif select=="look" and 4 in room and cloud==True:
            print("The weather it`s too cloudy, the place seems to be empty")

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

        elif select=="end" and 4 in room:
            count = {"room": room, "sword": "sword" in inventory, "shield": "shield" in inventory, "boots": "boots" in inventory, "username":s1_options, "game name":game_set}

            end_ses(count)
            print("You eneded the session, your data was saved")
            room=set()
            life=0

        else:
            pass


    while 3 in room:  #Entering room 3
        print("There is a dragon in the room")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("do you want to fight or go to the door in the right or the door in the left, choose 'fight', 'right', 'left', 'front','check' or 'end': '")

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

        elif select=="end" and 3 in room:
            count = {"room": room, "sword": "sword" in inventory, "shield": "shield" in inventory, "boots": "boots" in inventory, "username":s1_options, "game name":game_set}

            end_ses(count)
            print("You eneded the session, your data was saved")
            room=set()
            life=0

        else:
            pass

    while 8 in room:  #Entering room 8
        print("There is no oponent in this room")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("do you want to 'look' around or to go 'left' or 'front' door: choose 'look', 'left', 'front','check' or 'end' ")

        if select=="look" and 8 in room and cloud==False:
            inventory.add("boots")
            print("You found some 'boots', useful for protection against wild animals")

        elif select=="look" and 8 in room and cloud==True:
            print("The weather it`s too cloudy, the place seems to be empty")

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

        elif select=="end" and 8 in room:
            count = {"room": room, "sword": "sword" in inventory, "shield": "shield" in inventory, "boots": "boots" in inventory, "username":s1_options, "game name":game_set}

            end_ses(count)
            print("You eneded the session, your data was saved")
            room=set()
            life=0

        else:
            pass

    while 7 in room:  #Entering room 7
        
        print("There is a evil wizard in the room, you can`t beat him by your own")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("do you want to 'fight'  or to go 'left' or 'right' door: choose 'fight', 'left','right','check' or 'end' ")

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

        elif select=="end" and 7 in room:
            count = {"room": room, "sword": "sword" in inventory, "shield": "shield" in inventory, "boots": "boots" in inventory, "username":s1_options, "game name":game_set}

            end_ses(count)
            print("You eneded the session, your data was saved")
            room=set()
            life=0

        else:
            pass

    while 6 in room:   #Entering room 6

        if x==1 and 6 in room and multi_==False:
            multiplayer=True
            print("congratulations you found a partner who will help you during the game")

        elif x==2 and 6 in room and multi_==False:
            multiplayer=False

        print("There is no oponent in this room")
        print("\n")
        print("Your inventory status: ",inventory, "you can check it by choosing 'check'")
        select=input("You can go to 'right' or 'front' door: choose 'right','front','check' or 'end'")
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

        elif select=="end" and 6 in room:
            count = {"room": room, "sword": "sword" in inventory, "shield": "shield" in inventory, "boots": "boots" in inventory, "username":s1_options, "game name":game_set}

            end_ses(count)
            print("You eneded the session, your data was saved")
            room=set()
            life=0



















