#pengujian jenis jenis error

#syntax error

# print("hello world" 

#ini merupakan syntax error karena ada kesalahan dalam menuliskan syntax yang dimana harusnya ada kurung tutupnya
#jika di print maka akan ada tulisan syntax error.

#NameError

print(nama)

nama = "ghaniar"

#error ini akan timbul ketika kita akan memanggil variabel yang belum terdeklarasi
#jika di print akan muncul tulisan NameError 'nama' was not defined

#TypeError

hitungan = "5" + 5

print(hitungan)

#error ini saat melakukan oprasi pada tipe data yang tidak sesuai
#output yang akan ditampilkan adalah tulisan TypeError

#ValueError 

a = int("abc")

print(a)
#error ini akan terjadi jika kita mengkonversi tipe data dengan yang tidak seharusnya, misalnya kita ingin menggubah dari string ke bentuk 
# integer tetapi si valuenya itu tidak mengibaratkan sebuah integer


#indexerror

buah = ["apel", "jeruk", "pisang"]

print(buah[3])

#eror ini akan terjadi disaat mengakses suatu list atau tuple yang indexnya tidak ada dalam list tersebut

#keyerror

siswa = {
   "nama": "Alice",
    "umur": 20,
   "kelas": "12A"
}

print(siswa["tinggi_badan"])

#sama seperti indexerrr akan error jika kita memanngil hal yang tidak ada dalam dictionary, maka akan terjadi error

#ZeroDivisionError

#eror yang akan terjadi jika ada oprasi pembagian dengan 0

pembagian = 12 / 0

#print(pembagian)

#try and except

try :
   print (100/0)
except :
    
#pada saat  perintah di eksekusi nanti python akan melihat apakah itu error atau bukan jika error maka akan langsung mengeksekusi blok except

# try:
#     a = int(input("Masukkan angka pertama: "))
#     b = int(input("Masukkan angka kedua: "))
#     hasil = a / b
#     print("Hasil pembagian:", hasil)
# except ValueError:
#     print("Mohon masukkan angka yang valid!")
# except ZeroDivisionError:
#     print("Tidak bisa dibagi dengan nol!")
# except:
#     # print("Terjadi kesalahan yang lain!")



try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input tidak valid!")
else:
    print("Angka yang Anda masukkan:", angka)
    if angka > 0:
        print("Angka positif")
    elif angka < 0:
        print("Angka negatif")
    else:
        print("Angka nol")
finally:
    print("Program selesai dijalankan")

