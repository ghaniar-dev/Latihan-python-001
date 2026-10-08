def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius * radius
    return luas

luas1 = hitung_luas_lingkaran(5)
luas2 = hitung_luas_lingkaran(10)

print("Luas lingkaran radius 5:", luas1)
print("Luas lingkaran radius 10:", luas2)
print("Total luas gabungan:", luas1 + luas2)