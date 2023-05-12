
stringNumber = 1

with open("results.txt") as f:
    for line in f:
        print(stringNumber + ". " + line)
        stringNumber += 1
