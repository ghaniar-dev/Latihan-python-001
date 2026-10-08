# List dasar dan manipulasi
daftar_kosong = []
angka = [1, 2, 3, 4, 5]
nama = ["Alice", "Bob", "Charlie"]
campuran = ["Alice", 25, "Bob", 30]

buah = ["apel", "jeruk", "pisang", "mangga"]
print(buah[0])
print(buah[-1])

warna = ["merah", "biru", "hijau"]
warna[1] = "kuning"

buah.append("pisang")
angka.remove(3)
angka.pop()
del angka[0]

gabungan = [1, 2, 3] + [4, 5, 6]

for item in buah:
    print("-", item)

for i in range(len(buah)):
    print(str(i + 1) + ".", buah[i])


    # Tuple
point = (5, 10)
tanggal_lahir = (15, 8, 1990)
for e in tanggal_lahir:
    print(e)

# Dictionary
siswa = {"nama": "Alice", "umur": 20, "kelas": "12A"}
siswa["umur"] = 21
del siswa["kelas"]

for key, value in siswa.items():
    print(key, "=", value)

# Set
buah_set = {"apel", "jeruk", "pisang"}
buah_set.add("mangga")
buah_set.add("mangga")
buah_set.remove("jeruk")

#penerapan
nilai_siswa = [85, 92, 78, 90, 65, 88]
jumlah_siswa = len(nilai_siswa)
total_nilai = sum(nilai_siswa)
rata_rata = round(total_nilai / jumlah_siswa, 2)
nilai_tertinggi = max(nilai_siswa)
nilai_terendah = min(nilai_siswa)

penjual = ["Budi", "Andi", "Citra", "Dewi"]
penjualan = [15, 42, 23, 31]
data_toko = list(zip(penjualan, penjual))
data_terurut = sorted(data_toko, reverse=True)

for rank, (jumlah, nama_p) in enumerate(data_terurut, start=1):
    print(f"Juara {rank}: {nama_p} dengan penjualan {jumlah} barang")


    # Scope Variable
nama_global = "Alice"
def ubah_nama():
    global nama_global
    nama_global = "Bob"

# Parameter Dinamis
def list_dict(*list_data, **dict_data):
    print(list_data)
    print(dict_data)

# Map, Filter, dan Lambda
list_negara = ['Indonesia', 'Jerman', 'Qatar', 'Australia', 'Prancis']
is_str = lambda x: type(x) == str
negara_filtered = list(filter(is_str, list_negara))

angka_list = [5, 12, 17, 18, 24]
angka_genap = list(filter(lambda x: x % 2 == 0, angka_list))
angka_dikali_dua = list(map(lambda x: x * 2, angka_list))