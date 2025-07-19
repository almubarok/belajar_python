# count = 0
# while True:
#   if count == 5:
#     break
#   print(count)
#   # count = count + 1
#   count += 1

# for i in range(-1, 5):
#   print(i)

def is_valid_number(n):
  return n % 3 == 0 and n % 4 != 0


datas = [9,12,18,24,17]

# for data in datas:
#   print(f"bilangan {data} is_valid_number?", is_valid_number(data))

n = input()
print("input kamu:", n)



# *
# **
# ***
# ****
# *****
# ******

#    *
#   ***
#  *****
# *******




def is_valid_number(n):
  return n % 3 == 0 and n % 4 != 0

def all_valid_number(start, end):
  pass

all_valid_number(1,10)
# Output:
# 1: False
# 2: False
# 3: True
# 4: False
