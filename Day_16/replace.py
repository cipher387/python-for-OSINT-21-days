def replaceDash(x):
  return x.replace("_","-")

words = ["six_pack","king_size","editor_in_chief"]

result = map(replaceDash,words)

print(list(result))
