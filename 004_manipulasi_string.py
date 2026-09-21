#string dan manipulasi string
#string merupakan tipe data untuk menyimpan karakter 
#untuk menggabungkan string bisa menggunakan tanda + (tambah)
#string tidak bisa digabungkan dengan tipe data lain

nama = "ghaniar"
umur = 20

print ("nama saya "+ nama + " dan umur saya " + str(umur))

pesan = "nama saya " + nama + " dan Umur saya " + str(umur)

print (pesan)
print (type(pesan))

print (umur + umur)

print (len(nama))


#mengakses karakter dalam string (indexing)
# 1. setiap karakter dalam string memiliki posisi (index) yang di mulai dari 0
# 2. untuk mengakses tiap karakter di string, kita bisa gunakan kurung kotak dan didalam kurung kotak tersbut disebutkan posisinya
# 3. bisa ngambil dari belakang kalo pake negatif