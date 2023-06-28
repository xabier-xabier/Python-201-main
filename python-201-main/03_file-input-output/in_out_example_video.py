
words=[]

with open("words.txt","r") as fin:
    for word in fin.readlines():
        word=word.rstrip()
        words.append(word)


far_list =[]
for w in words:
    if w.startswith("far"):
        far_list.append(w)


with open("far.txt","w") as fout:
    fout.write("\n".join(far_list))