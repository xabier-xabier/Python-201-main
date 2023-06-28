# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

from pathlib import Path
import csv

data_path=Path("/Users/sagar/OneDrive/Escritorio/file-counter")


with open(data_path.joinpath("filecounts.csv"), "r") as file_in:
    print(file_in.read())


count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open(data_path.joinpath("filecounts2.csv"), "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)



