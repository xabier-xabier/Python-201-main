# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

words=[]
with open("words.txt","r") as fin:
    for f in fin.readlines():
        txt=f[::-1]
        words.append(txt)
        

with open("words_reverse.txt","w") as fout:
    fout.write("\n".join(words))