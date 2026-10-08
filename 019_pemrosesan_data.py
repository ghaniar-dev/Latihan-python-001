angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

angka_genap = list(filter(lambda x: x % 2 == 0, angka))
hasil_kali = list(map(lambda x: x * 10, angka_genap))

print("Angka awal:", angka)
print("Hasil filter genap:", angka_genap)
print("Hasil map (x10):", hasil_kali)