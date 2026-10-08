buah = ["apel", "jeruk", "pisang"]
buah.append("mangga")
buah[1] = "anggur"
buah.remove("pisang")

print("List akhir:", buah)
print("Jumlah buah:", len(buah))

for item in buah:
    print("-", item)