#string interpolation
#untuk  menggabungkan variabel dengan teks, menggunakan kurung kurawal

nama = "Ghaniar"
umur = 20
kota = "Sumedang"
tinggi_badan = 190.5

biodata = f"Nama \t: {nama}\nUmur \t: {umur}\nKota \t: {kota}\nTB \t: {tinggi_badan}"
print(biodata)
"\n"
"\n"
#dalam fstring dapat menambahkan methods dan juga operasi di dalamnya
biodata1 = f"Nama \t: {nama.upper()}\nUmur \t: {umur+100}\nKota \t: {kota.replace("Sumedang","Bandung")}\nTB \t: {tinggi_badan}"
print(biodata1)

#tugas buat jadi 1 variable outputnya, tambahkan url kampus, tambahkan path folder tugasnya, tambahkan nama panggilan pake teknik slicing, tambahkan 1 methods dan 1 operasi