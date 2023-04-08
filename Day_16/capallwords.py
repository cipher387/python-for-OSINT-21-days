def capitalizeAllWords(x):
  return x.title()

cities = ["new york","los angeles","chicago"]

result = map(capitalizeAllWords,cities)

print(list(result))
