def filter_odd_multiples_of_three(start, end):
  jawaban = []
  for number in range(start, end+1):
    if number % 2 != 0 and number % 3 == 0:
      jawaban.append(number)
  print(f"Ditemukan {len(jawaban)}: {jawaban}")

filter_odd_multiples_of_three(10,33)
# Output: Ditemukan 3 bilangan: [15, 21, 27, 33]
