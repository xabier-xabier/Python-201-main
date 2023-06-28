# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

tup_i=tuple(string)

list_i=list(tup_i)

list_i[0]="k"

tup_f=tuple(list_i)

print(tup_f)

