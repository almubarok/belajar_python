def is_valid_number(n):
  return n % 3 == 0 and n % 4 != 0

print(is_valid_number(9))
print(is_valid_number(12))
print(is_valid_number(18))
print(is_valid_number(24))
print(is_valid_number(17)) # false
