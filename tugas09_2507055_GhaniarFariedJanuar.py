#Ghaniar faried januar
#2507055
#3B

print("=== VERIFIKASI KASIR ===")
# Input nama kasir lalu diurai karakternya satu per satu
nama_kasir = input("Masukkan nama kasir yang bertugas: ")

# For String: Mengurai nama kasir huruf demi huruf
for huruf in nama_kasir:
    print(f"Verifikasi ID Karakter: {huruf.upper()}")


print("\n=== PENGECEKAN AREA TOKO ===")
input("Tekan Enter untuk mulai pengecekan rak toko...")
jumlah_lantai = 2
jumlah_rak_per_lantai = 2

# Nested Loop: Loop bersarang untuk cek area toko sebelum melayani
for lantai in range(1, jumlah_lantai + 1):  # Loop luar
    for rak in range(1, jumlah_rak_per_lantai + 1):  # Loop dalam
        print(f"[OK] Memeriksa Ketersediaan Rak di Lantai {lantai} - Rak {rak}")


print("\n=== PENGECEKAN KODE DISKON ===")
daftar_voucher = ["DISCO10", "HEMAT20", "SUPER50"]
voucher_user = input("Masukkan kode voucher diskon (jika ada): ").upper()

for voucher in daftar_voucher:
    if voucher == voucher_user:
        print(f"Selamat! Voucher '{voucher_user}' berhasil digunakan.")
        break  
# For Else: Berjalan jika perulangan selesai tanpa terkena perintah 'break'
else:
    print(
        f"Voucher '{voucher_user}' tidak ditemukan atau tidak valid. Lanjut tanpa diskon."
    )


print("\n=== PROSES ANTREAN & TRANSAKSI PELANGGAN ===")
# Input jumlah total orang yang mengantri
total_orang = int(input("Masukkan jumlah orang yang mengantri: "))
nomor_antrean = 1

# While Loop Utama: Berjalan selama masih ada orang dalam antrean
while total_orang > 0:
    print(f"\n==================================================")
    print(
        f"MELAYANI PELANGGAN ANTREAN KE-{nomor_antrean} (Sisa Antrean: {total_orang - 1} orang)"
    )
    print(f"==================================================")

    # List untuk menyimpan daftar nama dan harga barang pelanggan saat ini
    daftar_nama_barang = []
    daftar_harga_barang = []
    total_belanja = 0

    # While Loop Transaksi: Untuk input banyak barang per pelanggan
    while True:
        nama_barang = input(
            "\nMasukkan nama barang (ketik 'selesai' untuk bayar): "
        )

        if nama_barang.lower() == "selesai":
            print(">> Input barang selesai. Menghitung rincian transaksi...")
            break

        input_harga = input(f"Masukkan harga untuk '{nama_barang}': ")
        harga_barang = int(input_harga)

        if harga_barang == 0:
            print(f">> Barang '{nama_barang}' bernilai Rp0 (Bonus/Gratis), dilewati dari total.")
            continue

        # Simpan nama dan harga ke dalam list
        daftar_nama_barang.append(nama_barang)
        daftar_harga_barang.append(harga_barang)
        total_belanja += harga_barang

        print(
            f">> '{nama_barang}' (Rp{harga_barang}) berhasil ditambahkan! Subtotal: Rp{total_belanja}"
        )

    # Menampilkan rincian barang yang dibeli pelanggan
    print(f"\n--- RINCIAN BELANJA PELANGGAN KE-{nomor_antrean} ---")
    if len(daftar_nama_barang) == 0:
        print("Tidak ada barang yang dibeli.")
    else:
        # For Loop untuk menampilkan pasangan nama barang dan harga
        for i in range(len(daftar_nama_barang)):
            print(
                f"- {daftar_nama_barang[i]} : Rp{daftar_harga_barang[i]}"
            )

    print(f"TOTAL BAYAR: Rp{total_belanja}")
    print(
        f"\n[INFO] Antrean pelanggan ke-{nomor_antrean} telah SELESAI dilayani!"
    )

    # Perbarui penghitung antrean
    total_orang -= 1  # Dekremen (pengurangan nilai variabel) sisa antrean
    nomor_antrean += 1  # Naikkan nomor antrean berikutnya

# While Else: Dijalankan otomatis saat antrean habis (total_orang > 0 bernilai False)
else:
    print("\n==================================================")
    print("[SELESAI] Semua pelanggan dalam antrean telah selesai dilayani!")
    print("Terima kasih sudah bertugas hari ini!")
    print("==================================================")