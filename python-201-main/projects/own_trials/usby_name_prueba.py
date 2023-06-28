import requests

#min_len = 4
#max_len = 12
#URL = f"https://uzby.com/api.php?min={min_len}&max={max_len}"

#response = requests.get(URL)
#print(response.text)


def call_name(name):
    min=4
    max=len(name)
    URL = f"https://uzby.com/api.php?min={min}&max={max}"
    response = requests.get(URL)

    return response.text

text=input("Please choose a name between 4 and 12 characters: ")

text_in=False
while text_in==False:
    if len(text)>=4 and len(text)<=12:
        game_name=call_name(text)
        print(f"Your game name is: {game_name}")
        text_in=True

    else:
        text=input("Please choose a name between 4 and 12 characters: ")
