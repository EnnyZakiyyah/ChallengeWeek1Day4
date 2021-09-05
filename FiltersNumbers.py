print("Filters Numbers".center(75, "="))

print("Input Awal Tahun")
awalTahun = int(input())
print("Input Akhir Tahun")
akhirTahun = int(input())

print("\nCetak List leap years:")
for tahun in range(awalTahun, akhirTahun):
    if (0 == tahun % 4) and (0 != tahun % 100) or (0 == tahun % 400):
        print(tahun)
