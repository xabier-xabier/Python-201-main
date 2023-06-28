# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

text=input("please write a text: ")

lon=len(text)
dictionary={}

for i in range(0,lon,1):
    cont=text.count(text[i])
    dictionary[text[i]]=cont


print(dictionary)

