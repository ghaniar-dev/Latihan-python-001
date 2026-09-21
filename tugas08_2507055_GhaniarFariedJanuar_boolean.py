#output untuk pilihan operator
print(f"======= Kalkulator Sederhana ======= \n1. Penjumalahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n")

#input untuk angk yang akan di hitung
pilihan = int(input("Pilih operator (1-4): "))
a = float(input("Masukan Angka Pertama: "))
b = float(input("Masukan Angka Kedua: "))
c = float(input("Masukan Angka ketiga: "))

#agar pembaginya tidak sama dengan 0
bagiaman_b = b + (b == 0)   
bagiaman_c = c + (c == 0)

#logika boolean untuk menetukan pilihan operator
tambah = pilihan == 1       #akan true jika pilihan = 1
pengurangan = pilihan == 2  #akan true jika pilihan = 2
perkalian = pilihan == 3    #akan true jika pilihan = 3
pembagian = pilihan == 4    #akan true jika pilihan = 4

#jadi nanti yang jika yang true maka akan bernilai 1 dan yang false akan bernilai 0

hasil = (a + b + c) *tambah                 
+ (a - b - c) *pengurangan 
+ (a * b * c) *perkalian 
+ (a / bagiaman_b / bagiaman_c) *pembagian

#nah ini nanti bentuknya akan seperti ini, jika pilihan = 1, a = 1, b = 1, c= 1
# (1 + 1 + 1) *1 + (1- 1- 1 )*0 + (1 * 1 * 1) *0 + (1 / 1 / 1) *0
# (3)*1 + 0 + 0 + 0
# hasil nya kita seperti yang di harapkan dari penjumlahan 

print(f"hasil dari perhitungan : {hasil}")

