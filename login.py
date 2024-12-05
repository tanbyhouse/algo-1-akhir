import pandas as pd
import os
import csv

def selamat_datang():
    print("""
    ==========================================
                SELAMAT DATANG   
    ==========================================
    """)


def selamat_datang():
    print("=== Selamat Datang===")

def register():
    try:
        if os.path.exists("users.csv"):
            users = pd.read_csv("users.csv")
        else:
            print("File Users.csv tidak ditemukan")

        print("=== Registrasi Akun Baru ===")
        username = input("Masukkan username: ")

        if username == "":
            print("Username tidak bisa kosong")
            input("Tekan Enter untuk kembali...")
            return
        
        elif username in users['username'].values:
            print("Username sudah terdaftar. Silakan gunakan username lain.")
            input("Tekan Enter untuk kembali...")
            return

        password = input("Masukkan password: ")
        konfirmasi_password = input("Konfirmasi password: ")

        if password != konfirmasi_password:
            print("Password tidak cocok. Silakan coba lagi.")
            input("Tekan Enter untuk kembali...")
            return

        role = "pembeli"

        new_user = pd.DataFrame([{
            "username": username,
            "password": password,
            "role": role
        }])
        users = pd.concat([users, new_user], ignore_index=True)
        users.to_csv("users.csv", index=False)

        print(f"Akun berhasil didaftarkan untuk {username} sebagai {role}.")
        input("Tekan Enter untuk kembali ke menu...")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        input("Tekan Enter untuk kembali ke menu...")

def login():
    while True:
        selamat_datang()
        print("""
        Pilih opsi:
        1. Login
        2. Register
        3. Keluar
        """)

        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            print("""
            Pilih login sebagai:
            1. Admin
            2. Pembeli
            3. Kembali
            """)
            pilih_login = input("Pilih (1/2/3): ")

            if pilih_login == '1':
                peran = "admin"
            elif pilih_login == '2':
                peran = "pembeli"
            elif pilih_login == '3':
                continue
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                input("Tekan Enter untuk melanjutkan...")
                continue

            try:
                if os.path.exists("users.csv"):
                    users = pd.read_csv("users.csv")
                else:
                    print("Tidak ada akun yang terdaftar. Silakan lakukan registrasi terlebih dahulu.")
                    input("Tekan Enter untuk kembali...")
                    continue

                print(f"\nAnda memilih login sebagai {peran}.")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")

                if username in users['username'].values:
                    data_user = users[users['username'] == username]

                    if password == data_user['password'].values[0]:
                        if data_user['role'].values[0] == peran:
                            print(f"Login berhasil! Selamat datang, {username}.")
                            input("Tekan Enter untuk melanjutkan...")
                            return peran
                        else:
                            print("Login gagal. Anda tidak memiliki akses sebagai", peran)
                    else:
                        print("Password salah. Silakan coba lagi.")
                else:
                    print("Username tidak ditemukan. Silakan coba lagi.")
            
            except FileNotFoundError:
                print("Error: File 'users.csv' tidak ditemukan. Pastikan file tersedia.")

            input("Tekan Enter untuk kembali ke menu...")
        elif pilihan == '2':
            register()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem kami.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")

login()