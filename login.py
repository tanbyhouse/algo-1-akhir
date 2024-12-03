import pandas as pd
import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def selamat_datang():
    print("""
    ==========================================
                SELAMAT DATANG   
    ==========================================
    """)

def login():
    while True:
        bersihkan_layar()
        selamat_datang()
        print("""
        Pilih login sebagai:
        1. Admin
        2. Pembeli
        3. Keluar
        """)
        
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            peran = "admin"
        elif pilihan == '2':
            peran = "pembeli"
        elif pilihan == '3':
            print("Terima kasih")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")
            continue

 
        try:
            users = pd.read_csv("users.csv")
            print(f"\nAnda memilih login sebagai {peran}.")
            
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            if username in users['username'].values:
                data_user = users[users['username'] == username]

                if password == data_user['password'].values[0]:
                    if data_user['role'].values[0] == peran:
                        bersihkan_layar()
                        print(f"Login berhasil! Selamat datang, {username}.")
                        input("Tekan Enter untuk melanjutkan...")
                    else:
                        print("Login gagal. Anda tidak memiliki akses sebagai", peran)
                else:
                    print("Password salah. Silakan coba lagi.")
            else:
                print("Username tidak ditemukan. Silakan coba lagi.")
        
        except FileNotFoundError:
            print("Error: File 'users.csv' tidak ditemukan. Pastikan file tersedia.")

        input("Tekan Enter untuk kembali ke menu...")

login()
print(f'adam')