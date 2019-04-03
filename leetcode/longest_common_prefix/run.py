

def main(arr):
    common = []
    try:
      first = arr[0]
      for i, c in enumerate(first):
          for w in arr:
              if first[i] != w[i]:
                  return "".join(common)
          common.append(c)
    except IndexError:
        return "".join(common)

    return "".join(common)


output = main(["flower", "flow", "flight"])
print("\"%s\"" % output)

output = main(["dog", "racecar", "car"])
print("\"%s\"" % output)

output = main(["aa", "ab"])
print("\"%s\"" % output)

output = main(["aa", "a"])
print("\"%s\"" % output)