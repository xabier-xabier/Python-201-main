# Using f-strings, print out the name, last name, and favorite
# office supply item of each person in the given dictionary,
# formatted like so:
#
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

# print LASTNAME, Name           Office supply item

for i in office:
    name_=i["full_name"]
    cut=name_.split()
    name=cut[0]
    last=cut[1]
    item=i["item"]
    print(f" LASTNAME: {last}, Name: {name}    office supply item: {item}")



# print LONGERLASTNAME, Name     Office supply item
# Create a new dictionary only with names and its surname length by reverse order
new_dict={}


for i in office:
    name_=i["full_name"]
    cut=name_.split()
    name=cut[0]
    last=cut[1]
    long=len(last)
    i["length"]=long
    new_dict[name+" "+last]=long
    

#print(new_dict)

sorted_dict=sorted(new_dict.items(), key=lambda x:x[1],reverse=True)
conv_dict=dict(sorted_dict) # back to dictionary

print(conv_dict)

# Identify the items by the previous names ordered by reverse order and print info
for i in conv_dict:
    for j in office:
        name_=j["full_name"]
        if name_==i:
            cut=name_.split()
            name=cut[0]
            last=cut[1]
            item=j["item"]
            print(f" LONGERLASTNAME: {last}, Name: {name}    office supply item: {item}")

        else:
            pass






