# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.

from pathlib import Path
import csv
import json
import textwrap


data_path=Path("/Users/sagar/OneDrive/Escritorio/file-counter")

# First CSV file to read and write
with open(data_path.joinpath("filecounts.csv"), "r") as file_in:
    print(file_in.read())


count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open(data_path.joinpath("filecounts2.csv"), "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)


# Second JSON file to read and write
with open(data_path.joinpath("filecounts.json"), "r") as file_in:
    print(file_in.read())

json_object=json.dumps(count, indent=4)
with open(data_path.joinpath("filecounts2.json"), "a") as jsonfile:
    jsonfile.write(json_object)



#Third txt file to read and write
with open(data_path.joinpath("filecounts.txt"), "r") as file_in:
    print(file_in.read())
    text=str(file_in.read())

with open(data_path.joinpath("filecounts2.txt"), "a") as txtfile:
    txtfile.write(json.dumps(count))

    

