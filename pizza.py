import csv
import sys
from tabulate import tabulate

table = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif '.csv' not in sys.argv[1]:
    sys.exit('Not a CSV file')

new_list = []

with open(sys.argv[1], 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        table.append(row)
    print(tabulate(table[1:], headers=table[0], tablefmt='grid'))

