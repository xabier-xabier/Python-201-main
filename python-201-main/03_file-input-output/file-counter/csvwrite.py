# Write the file counts to a `.csv` file.

import csv
# -- snip --
count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open("filecounts1.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)