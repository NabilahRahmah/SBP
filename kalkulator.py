a = 10
b = 20
c = a + b
print(c)

print("++++++++++++++++++++++++++++++")
print("===== Pilih Operasi =====")
print("1. Perkalian")
print("2. Penambahan")
print("3. Pembagian")
print("4. Pengurangan")

pilihan = input("Masukkan pilihan (1/2/3/4): ")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    print("Hasil:", angka1 * angka2)
elif pilihan == '2':
    print("Hasil:", angka1 + angka2)
elif pilihan == '3':
    print("Hasil:", angka1 / angka2)
elif pilihan == '4':
    print("Hasil:", angka1 - angka2)
else:
    print("Input tidak valid")