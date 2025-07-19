def penjumlahan(angka1, angka2):
  return angka1 + angka2

def perkalian(angka1, angka2):
  return angka1 * angka2

def luas_persegi_panjang(p, l):
  return perkalian(p, l)

hasil = penjumlahan(5, 8)
print(hasil)
print(luas_persegi_panjang(6,9))

# x = 6
# if x > 0 and (not x % 3 == 0):
#   print("lebih dari 0")
# elif x < 0:
#   print("kurang dari 0")



a = 2
b = 3
prosess = 'asdad'

if prosess in list_prosess:
  if prosess == 'perkalian':
    print(perkalian(a,b))
  elif prosess == 'penjumlahan':
    print(penjumlahan(a,b))
else:
  print("proses invalid")
  
  
  
  
ls = [1, 2, 3, 4, 5]
st = "abcdefghij"
print(ls[0])

print(f"ini data index 2{ls[2]}")
print(ls[:4])
print(st[3:6])

