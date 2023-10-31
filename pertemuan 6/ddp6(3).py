Jumlah_baris = int(input("Masukkan Jumlah Baris: "))

for i in range(1, Jumlah_baris + 1):
    for j in range(i):
        print("*", end=" ")
    print()