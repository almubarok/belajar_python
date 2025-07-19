# good number adalah bilangan genap dan kelipatan 13.
# buat code untuk cek apakah good number atau bukan

def is_good_number(n):
  return n % 2 == 0 and n % 13 == 0

print(is_good_number(2)) # false
print(is_good_number(13)) # false
print(is_good_number(26)) # true
print(is_good_number(30)) # false
print(is_good_number(52)) # true
