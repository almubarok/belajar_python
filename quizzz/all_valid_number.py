def is_valid_number(n):
  return n % 3 == 0 and n % 4 != 0

# def all_valid_number(start, end):
#   for i in range(start, end+1):
#     print(i, ":", is_valid_number(i))
#     # print(f"{i}:")

def all_valid_number(start, end):
  for i in range(start, end+1):
    print(i, ":", i % 3 == 0 and i % 4 != 0)
    # if i % 3 == 0 and i % 4 != 0:
    #   print(i, ":", "True")
    # else:
    #   print(i, ":", "False")

all_valid_number(1,10)