# Data mahasiswa
mahasiswa = [
    {"nama": "helmiati", "nilai": 87},
    {"nama": "azxhizriati", "nilai": 75},
    {"nama": "dinda", "nilai": 66},
    {"nama": "aya", "nilai": 59},
    {"nama": "fikra", "nilai": 45},
    {"nama": "Fajar", "nilai": 39}
]

# Fungsi konversi nilai ke huruf
def konversi_nilai(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 80:
        return "A-"
    elif nilai >= 75:
        return "B+"
    elif nilai >= 70:
        return "B"
    elif nilai >= 65:
        return "B-"
    elif nilai >= 60:
        return "C+"
    elif nilai >= 55:
        return "C"
    elif nilai >= 50:
        return "D"
    elif nilai >= 40:
        return "E"
    else:
        return "E (Tidak Lulus)"

# Menampilkan tabel
print("{:<10} {:<10} {:<10}".format("Nama", "Nilai", "Grade"))
print("-" * 30)
for mhs in mahasiswa:
    grade = konversi_nilai(mhs["nilai"])
    print("{:<10} {:<10} {:<10}".format(mhs["nama"], mhs["nilai"], grade))