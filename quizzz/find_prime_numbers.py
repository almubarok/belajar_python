# buatlah code untuk mencetak n bilangan prima
def is_prime(n):
  if n < 2:
    return False
  
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def find_prime_numbers(n):
	# your code here!
  found = 0
  counter = 2
  ans = []
  while found != n:
    is_found = is_prime(counter)
    if is_found:
      ans.append(counter)
      found += 1
    counter += 1
  return ans

#halohalo
print(find_prime_numbers(5))
# Output: [2,3,5,7,11]
