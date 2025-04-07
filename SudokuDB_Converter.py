import csv
import json

try:
    with open('sudoku.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        puzzles = [{"puzzle": row["puzzle"], "solution": row["solution"]} for row in reader]
    with open('sudoku.json', 'w') as json_file:
        json.dump(puzzles, json_file, indent=2)
except:
    print("Something went wrong..")
else:
    print("Successful conversion!")