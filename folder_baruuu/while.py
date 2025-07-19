# kelipatan 4 angka kelipatan 3 

def find():
  found = 0
  counter = 0
  ans = []
  while True:
    counter += 1
    if counter % 3 == 0:
      found += 1
      ans.append(counter)
    if found == 4:
      return ans

print(find())

# found = 0
# counter = 0
# while found != 4:
#   counter += 1
#   if counter % 3 == 0:
#     found += 1
#     print(f"{found}, {counter}")
