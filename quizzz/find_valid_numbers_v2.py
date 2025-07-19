# valid number adalah angka yang habis dibagi 3 tapi tidak habis dibagi 4
# cari n bilangan valid number pertama setelah m


def find_valid_numbers_v2(n, m):
		valid_numbers = []
		current = m + 1  # Start checking from the number after m

		while len(valid_numbers) < n:
				if current % 3 == 0 and current % 4 != 0:
						valid_numbers.append(current)
				current += 1

		return valid_numbers

print(find_valid_numbers_v2(5, 15))
# Output: [18, 21, 24, 27, 30]
