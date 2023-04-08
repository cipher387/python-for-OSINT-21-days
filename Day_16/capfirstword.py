def capitalizeFirstWord(x):
  return x.capitalize()

cities = ["new york","los angeles","chicago"]

result = map(capitalizeFirstWord,cities)

print(list(result))
