# valid number adalah angka yang habis dibagi 3 tapi tidak habis dibagi 4
# cari n bilangan valid number pertama

def find_valid_numbers(n):
		valid_numbers = []
		current = 1  # Start checking from the first number

		while len(valid_numbers) < n:
				if current % 3 == 0 and current % 4 != 0:
						valid_numbers.append(current)
				current += 1

		return valid_numbers



print(find_valid_numbers(5))
# Output: [3, 6, 9, 15, 18]
