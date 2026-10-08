penjual = ["Budi", "Andi", "Citra"]
penjualan = [15, 42, 23]

data_toko = list(zip(penjualan, penjual))
data_terurut = sorted(data_toko, reverse=True)

print("=== PAPAN PERINGKAT PENJUALAN ===")
for rank, (jumlah, nama) in enumerate(data_terurut, start=1):
    print(f"Juara {rank}: {nama} dengan penjualan {jumlah} barang")