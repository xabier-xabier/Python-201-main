
from random import randint

def get_hand(number):
    if number==0:
        text="scissors"

    elif number==1:
        text="rock"

    elif number==2:
        text="paper"
    
    else:
        print("your number is not between 0-2")

    return text


def determine_winner(hand,computer):
    if hand=="scissors":
        if computer=="scissors":
            print("It`s a draw..., you both chose 'scissors'")

        elif computer=="paper":
            print("You won!!! 'scissors' beats 'paper'")

        else:
            print("You loose... 'Rock' beats the 'scissors'")

    elif hand=="rock":
        if computer=="scissors":
            print("You won!! 'rock' beats 'scissors'")

        elif computer=="paper":
            print("You loose...'paper' beats 'rock'")

        else:
            print("It`s a draw. Both chose 'rock'")

    elif hand=="paper":
        if computer=="scissors":
            print("You loose...'scissors beat 'paper'")

        elif computer=="paper":
            print("It`s a draw. Both chose paper")

        else:
            print("You won. 'Paper' beats 'rock'")




print("Welcome to Rock-Paper-scissors game")
print("0=scissors, 1=rock and 2=paper")
text=int(input("Please choose a number between 0-2: "))
computer=randint(0,2)


hand=get_hand(text)
comp=get_hand(computer)
print("your hand is: ",hand)
print("the computer chose: ",comp)
print("\n")

determine_winner(hand,comp)
