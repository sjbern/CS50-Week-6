import sys, csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if '.csv' not in sys.argv[1]:
        print("Invalid file type")
    else:
        fileNameR = sys.argv[1]
        fileNameW = sys.argv[2]

output = []
with open(fileNameR, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        split = row['name'].split(',')
        output.append({'first':split[1].lstrip(), 'last':split[0], 'house':row['house']})

with open(fileNameW, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=['first','last','house'])
    writer.writerow({'first':'first', 'last':'last', 'house':'house'})
    for row in output:
        writer.writerow({'first': row['first'], 'last':row['last'], 'house': row['house']})