

def main(arr):
  common = set()
  first = arr[0]
  for c in first:
    # if c in all the words, continue
    # if c not in 1 word, break
    for w in arr:
      if c not in w:
        return common
      else:
        common.add(c)
  return common

output = main(["flower","flow","flight"])
print(output)

output = main(["dog","racecar","car"])
print(output)