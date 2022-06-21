import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if '.py' not in sys.argv[1]:
        print("Invalid file type")
    else:
        fileName = sys.argv[1]


with open(fileName, 'r') as file:
    count = 0
    for line in file:
        if line.lstrip().startswith('#'):
            pass
        elif line != "\n":
            count += 1


print(count)


