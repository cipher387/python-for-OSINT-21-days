
stringNumber = 1

with open("results.txt") as f:
    for line in f:
        print(str(stringNumber) + ". " + line)
        stringNumber += 1
