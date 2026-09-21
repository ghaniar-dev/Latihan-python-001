#mengakses karakter dalam string (indexing)
# 1. setiap karakter dalam string memiliki posisi (index) yang di mulai dari 0
# 2. untuk mengakses tiap karakter di string, kita bisa gunakan kurung kotak dan didalam kurung kotak tersbut disebutkan posisinya
# 3. bisa ngambil dari belakang kalo pake negatif

pesan = "python"

print (pesan[0])
print (pesan[1])
print (pesan[2])
print (pesan[3])
print (pesan[4])
print (pesan[5], "\n")

#string slicing 
#digunakan untuk mengambil sebagian dari string
#bisa menggunakan kurung kotak dimana dalam kurung kotak terdapat 2 posisi omdex dipisahkan oleh : (titik dua) iyu menujukan posisi awal dan akhit karakter yang ingin kita ambil

print (pesan [0:3]) # menampilkan pyt, kenapa berakhir di t pdahal ngambil nya itu sampe index ke 3 yang gimana itu h, karena index 3 nya di di potong
print (pesan [3:]) # ini akan menampilkan hon, karena pada default nya jika tidak di isi di akhirnya maka akan dari titik 3 sampai ke akhir


