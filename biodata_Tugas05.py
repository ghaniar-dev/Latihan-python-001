#deklarasi variabel biodata

nama = "ghaniar faried januar"
usia = 20
tinggi_badan = 171.5
berat_badan = 60.5
Alamat = "jl. cilembu no.69"
pekerjaan = "mahasiswa"
sudah_menikah = False
no_hp = "081234567890"
hobi = ["membaca", "basket", "bermain game", "berlari"]
makanan_favorit = ("nasi goreng", "mie ayam", "sate", "bakso")

#menampilkan biodata
print("===============================================")
print("                   Biodata Diri                ")
print("===============================================")
print(f"Nama            : {nama}")
print(f"Usia            : {usia}")
print(f"Tinggi Badan    : {tinggi_badan} cm")
print(f"Berat Badan     : {berat_badan} kg")
print(f"Alamat          : {Alamat}")
print(f"Pekerjaan       : {pekerjaan}")
print(f"Status Menikah  : {sudah_menikah}")
print(f"No. HP          : {no_hp}")
print(f"Hobi            : {', '.join(hobi)}")
print(f"Makanan Favorit : {', '.join(makanan_favorit)}")
print("===============================================")

#menampilkan tipe data variabel
print("Tipe Data Variabel")
print(f"Tipe data nama                  : {type(nama)}")  
print(f"Tipe data usia                  : {type(usia)}")
print(f"Tipe data tinggi_badan          : {type(tinggi_badan)}")
print(f"Tipe data berat_badan           : {type(berat_badan)}")
print(f"Tipe data Alamat                : {type(Alamat)}")
print(f"Tipe data pekerjaan             : {type(pekerjaan)}")
print(f"Tipe data sudah_menikah         : {type(sudah_menikah)}")
print(f"Tipe data no_hp                 : {type(no_hp)}")
print(f"Tipe data hobi                  : {type(hobi)}")
print(f"Tipe data makanan_favorit       : {type(makanan_favorit)}")