# print("belajar Python"

# print(skor)

# total = "10" + 20
# print(total)

# umur = int("dua puluh")

# kota = ["Bandung", "Jakarta"]
# print(kota[4])

# produk = {"nama": "Laptop", "harga": 7000000}
# print(produk["stok"])


# nilai = 50 / 0 
# print(nilai)

# try:
#     hasil = 250 / 0
#     print(hasil)
# except:
#     print("Operasi gagal: Tidak dapat membagi bilangan dengan angka nol!")

# try:
#     daftar_menu = ["Nasi Goreng", "Mie Ayam", "Bakso"]
#     pilihan = int(input("Pilih nomor menu (0 - 2): "))
    
#     print("Menu pilihanmu:", daftar_menu[pilihan])

# except ValueError:
#     print("Error: Harus masukan angka, jangan huruf!")

# except IndexError:
#     print("Error: Nomor menu tidak ada dalam daftar!")


try:
    angka_sembarang = int(input("Masukkan angka sembarang: "))
except ValueError:
    print("Gagal: Masukan yang Anda berikan bukan angka!")
else:
    print("Input berhasil diterima:", angka_sembarang)
    if angka_sembarang % 2 == 0:
        print("Kategori: Bilangan Genap")
    else:
        print("Kategori: Bilangan Ganjil")
finally:
    print("Proses evaluasi selesai.")