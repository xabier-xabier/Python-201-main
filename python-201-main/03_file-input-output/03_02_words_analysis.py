# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

lon=0
count=0
short=1000000000

# detect the length of the longest word
with open("words.txt","r") as fin:
    for f in fin.readlines():
        count+=1
        if len(f)>=lon:
            lon=len(f)
        else:
            pass

# detect the length of the shortest word
with open("words.txt","r") as fin:
    for f in fin.readlines():
        if len(f)<=short:
            short=len(f)
        else:
            pass



# print the longest words
print("These are the longest words:")
with open("words.txt","r") as fin:
    for f in fin.readlines():
        if len(f)==lon:
            print(f)
        else:
            pass

#print the shortest words
print("These are the shortest words")
with open("words.txt","r") as fin:
    for f in fin.readlines():
        if len(f)==short:
            print(f)
        else:
            pass

print("\n")
print("Total amount of words is: ",count)

