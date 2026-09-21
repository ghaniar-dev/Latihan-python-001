#operator aritmatika

x = 5
y = 4



print (x + y) #penjumlahan
print (x - y) #pengurangan 
print (x * y) #perkalian
print (x / y) #pembagian
print (x % y) #modulus
print (x ** y) #pangkat
print (x // y) #floor division

n = 10
print("Nilai n = ", n)

n += 5                  #ini sama kayak n = n + 5
print("Nilai n = ", n)

n -= 5                  #ini sama kayak n = n - 5
print("Nilai n = ", n)

n *= 5                  #ini sama kayak n = n * 5
print("Nilai n = ", n)

n /= 5                  #ini sama kayak n = n / 5
print("Nilai n = ", n)

n //= 5                 #ini sama kayak n = n // 5
print("Nilai n = ", n)

n %= 5                  #ini sama kayak n = n % 5
print("Nilai n = ", n)

n **= 5                 #ini sama kayak n = n ** 5
print("Nilai n = ", n)

# dengan catatan ini hanya mengganti isi data n nya saja dan di eksekusinya dari atas ke bawah


#operator perbandingan

x = 25
y = 40

print (x == y) #sama dengan
print (x != y) #tidak sama dengan
print (x > y) #lebih besar dari
print (x < y) #lebih kecil dari
print (x >= y) #lebih besar sama dengan
print (x <= y) #lebih kecil sama dengan

#opertor perbandingan logika

x = 50

print(x > 10 and x < 100) #akan bernilai true jika kedua kondisi terpenuhi
print(x > 10 or x < 100) #akan bernilai true jika salah satu kondisi terpenuhi
print(not(x > 10 and x < 100)) #akan bernilai true jika kondisi tidak terpenuhi
print(not(x > 10 or x < 100)) #akan bernilai true jika salah satu kondisi tidak terpenuhi

#operator string

nama_depan = "Ghaniar"
nama_belakang = "Faried"

nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

garis = "-" * 20
print(garis)

