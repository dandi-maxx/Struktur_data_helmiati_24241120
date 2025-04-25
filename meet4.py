# Program untuk mengecek bilangan
def cek_bilangan(bilangan):
    bil_str = str(bilangan)

    # Cek panjang bilangan harus minimal 4 digit (karena 2 digit awal dan 2 digit akhir)
    if len(bil_str) < 4:
        return "Bilangan terlalu pendek"

    dua_digit_awal = bil_str[:2]
    dua_digit_akhir = bil_str[-2:]

    if dua_digit_awal == "24" and dua_digit_akhir == "20":
        return f"{bilangan} memenuhi syarat (awal = 24, akhir = 20)"
    else:
        return f"{bilangan} TIDAK memenuhi syarat"

# Contoh pengujian
bilangan1 = 244520
bilangan2 = 24120
bilangan3 = 2420
bilangan4 = 24020
bilangan5 = 25120

print(cek_bilangan(bilangan1))  # Tidak memenuhi
print(cek_bilangan(bilangan2))  # Memenuhi
print(cek_bilangan(bilangan3))  # Memenuhi
print(cek_bilangan(bilangan4))  # Memenuhi
print(cek_bilangan(bilangan5))  # Tidak memenuhi