import pandas as pd

# Membaca file Excel
df = pd.read_excel('recipes.xlsx', sheet_name='Recipes')

# Fungsi untuk memproses data dan mengubah kolom Ingredients menjadi set
def proses_data(df):
    resep_list = []
    for _, row in df.iterrows():
        resep = {
            "nama": row['Name'],
            "bahan": set(row['Ingredients'].split(',')),
            "skor_nutrisi": row['NutritionScore']
        }
        resep_list.append(resep)
    return resep_list

# Mengubah data frame menjadi daftar resep
resep_list = proses_data(df)

# Fungsi untuk menemukan resep terbaik berdasarkan bahan yang tersedia menggunakan pendekatan Greedy
def cari_resep_terbaik(bahan_tersedia):
    resep_terbaik = None
    max_value_ratio = 0

    for resep in resep_list:
        bahan_cocok = resep["bahan"].intersection(bahan_tersedia)
        jumlah_cocok = len(bahan_cocok)
        
        # Menghindari pembagian dengan nol
        if jumlah_cocok > 0:
            value_ratio = resep["skor_nutrisi"] / jumlah_cocok
            # Pilihan greedy: berdasarkan rasio nilai terhadap jumlah bahan yang cocok
            if value_ratio > max_value_ratio:
                resep_terbaik = resep
                max_value_ratio = value_ratio

    return resep_terbaik

# Fungsi untuk mendapatkan input bahan dari pengguna
def dapatkan_bahan_pengguna():
    input_pengguna = input("Masukkan bahan yang Anda miliki (pisahkan dengan koma): ")
    bahan = set(map(str.strip, input_pengguna.split(',')))
    return bahan

# Mendapatkan input dari pengguna
bahan_pengguna = dapatkan_bahan_pengguna()

# Mencari resep terbaik
resep_terbaik = cari_resep_terbaik(bahan_pengguna)

# Menampilkan resep yang direkomendasikan
if resep_terbaik:
    print(f"Resep yang direkomendasikan untuk Anda adalah: {resep_terbaik['nama']}")
    print(f"Bahan yang dibutuhkan: {resep_terbaik['bahan']}")
    print(f"Skor nutrisi: {resep_terbaik['skor_nutrisi']}")
    print("Instruksi resep :")
    print("1. Potong bahan yang anda miliki sesuai selera")
    print("2. Ikuti instruksi pada bungkus mie instan")
    print("3. Rebus bahan bersamaan dengan mie instan")
    print("4. Sajikan bersama mie instan ")
    print("Catatan : Apabila bahan yang anda miliki tidak lengkap dengan resep maka skor nutrisi menyesuaikan dengan bahan anda")
else:
    print("Tidak ada resep yang cocok ditemukan.")
