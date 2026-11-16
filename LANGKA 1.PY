# --- 1. DEKLARASI DATA DIRI MAHASISWA ---
nim = 261080200031
nama_mahasiswa = "Ibel Maulana Abi Pratama"
semster = 1
is_aktif = True # Status registrasi ulang

# --- 2.  DATA NILAI MENTAH (Simulasi input dari form web / Database) ---
# Catatan: Input dari form seringkali terbaca sebagai string
str_nilai_algoritma = "85,5"
str_nilai_basis_data = "78.0"
str_nilai_pemrograman_web = "90.2" 
sks_per_matkul = 3 # Integer

# Tampilan data awal
print(f"Data Mahasiswa: {nama_mahasiswa} (NIM: {nim})")
print("Status Aktif :", is_aktif)