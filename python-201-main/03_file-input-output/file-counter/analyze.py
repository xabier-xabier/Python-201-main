# Use the `csv` module to read in and count the different file types.

# analyze.py
import csv

with open("filecounts.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

print(counts)