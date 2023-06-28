# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).



with open("words.txt","r") as fin:
    for f in fin.readlines():
        if len(f)>=20:
            print(f)

