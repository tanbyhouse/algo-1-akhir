import pandas as pd
import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    while True:
        print("""
        ============================
        Selamat datang di Program Login
        ============================
        Pilih login sebagai:
        1. Admin
        2. Pembeli
        3. Keluar
        """)

        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            role = "admin"
        elif pilihan == '2':
            role = "pembeli"
        elif pilihan == '3':
            print("Terima kasih, sampai jumpa lagi!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
            continue

        try:
            users = pd.read_csv("users.csv")  
            print(f"Login sebagai {role}")

            username = input("Masukkan username: ")
            if username in users['username'].values:
                barisuser = users[users['username'] == username]

                password = input("Masukkan password: ")
                if password == barisuser['password'].values[0]:
                    if barisuser['role'].values[0] == role:
                        bersihkan_layar()
                        print(f"Login berhasil sebagai {role}.")
                    else:
                        print(f"Login gagal! Anda bukan {role}.")
                else:
                    print("Password salah!")
            else:
                print("Username tidak ditemukan!")
        except FileNotFoundError:
            print("Error: File 'users.csv' tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

login()
