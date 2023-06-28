#clean the desktop
# get my tools
from pathlib import Path
import pprint

count_png=0
count_jpg=0
count_py=0
count_jpeg=0
count_pdf=0
count_doc=0
count_html=0
count_xls=0

dictionary={}

#locate the desktop
desktop = Path().home().joinpath("OneDrive\Escritorio")
print(desktop)


#identify type of files
for f in desktop.iterdir():
    if f.suffix==".png":
        count_png+=1
        
    elif f.suffix==".jpg":
        count_jpg+=1

    elif f.suffix==".py":
        count_py+=1

    elif f.suffix==".jpeg":
        count_jpeg+=1

    elif f.suffix==".pdf":
        count_pdf+=1

    elif f.suffix==".doc":
        count_doc+=1

    elif f.suffix==".html":
        count_html+=1

    elif f.suffix==".xls":
        count_xls+=1

    else:
        pass


# collect each type in a dictionary
dictionary={".png files":count_png , ".jpg files":count_jpg, ".py files":count_py, ".jpeg files":count_jpeg, ".pdf files":count_pdf,
            ".doc files":count_doc, ".html files":count_html, ".xls files":count_xls}

# print the dictionary
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dictionary)


#print the dictionary without pprint
#for i in dictionary:
    #print(i, dictionary[i])





