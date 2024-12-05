import pandas as pd
import os
import csv
import pyfiglet
from tabulate import tabulate

    #Variabel Global
poin_user = 0   
nilai_poin = 500  #Nilai 1 poin

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')


# def selamat_datang():
#     print('='*30)
#     print('         Selamat Datang    ')
#     print('='*30)
    
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
        bersihkan_layar()
        result = pyfiglet.figlet_format("Selamat Datang")
        print(result)

        print("""
Pilih opsi:
1. Login
2. Register
3. Keluar
""")
        pilihan = input("Pilih opsi (1/2/3): ")
        bersihkan_layar()
        if pilihan == '1':
            print("""
Pilih login sebagai:
1. Admin
2. Pembeli
3. Kembali
            """)
            pilih_login = input("Pilih (1/2/3): ")
            if pilih_login == "1":
                peran = "admin"
            elif pilih_login == '2':
                peran = "pembeli"
            elif pilih_login == '3':
                continue
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                input("Tekan enter untuk melajutkan...")
                continue
            
            try:
                if os.path.exists("users.csv"):
                    users = pd.read_csv("users.csv")
                else:
                    print("Tidak ada akun yang terdaftar. Silakan lakukan registrasi terlebih dahulu.")
                    input("Tekan enter untuk kembali...")
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
                            bersihkan_layar()
                            if peran == 'admin':
                                menu_admin()
                            elif peran == 'pembeli':
                                menu_pembeli()
                            # return peran
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
            result = pyfiglet.figlet_format("Terima Kasih")
            print(result)
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")
            
def baca_poin():
    try:
        poin_user = pd.read_csv("poin.csv")
        return int(poin_user['Poin User'].iloc[0])
    except FileNotFoundError:
        return 0 
    
def simpan_poin(poin):
    df = pd.DataFrame({'Poin User': [poin]})
    df.to_csv('poin.csv', index=False)

def checkout():
    total_produk = 0
    total_harga = 0 
    
    result = pyfiglet.figlet_format("Checkout")
    print(result)
    while True:
        try:
            produk = pd.read_csv('produk.csv')
        except FileNotFoundError:
            print('File tidak ditemukan')
            return
        teks = "Daftar Produk"
        print("="*30)
        print(f"{teks:^30}")
        print("="*30)
        
        # Menampilkan data sebagai tabel
        print(tabulate(produk, headers='keys', tablefmt='fancy_grid', showindex=False))
        
        try:
            pilih_produk = int(input('\nMasukkan ID produk yang ingin anda beli: '))
            if pilih_produk not in [i for i in produk['ID']]:
                print(f'ID {pilih_produk} tidak ditemukan. Silakan coba kembali')
                continue
            
            jumlah = int(input('Masukkan jumlah produk: '))
            if jumlah <= 0:
                print("Jumlah produk harus lebih dari 0.")
                continue
        except ValueError:
            print()
            print("Input harus berupa angka, Silakan ulangi kembali")
            continue
            
        harga_produk = produk.loc[produk['ID'] == pilih_produk, 'Harga Barang (Rp)'].iloc[0]
        nama_produk = produk.loc[produk['ID'] == pilih_produk, 'Nama Barang'].iloc[0]
            
        total_produk += int(jumlah)
        total_harga_produk = int(harga_produk*jumlah)
        total_harga += total_harga_produk
        bersihkan_layar()
        print()
        print(f'{jumlah} {nama_produk} ditambahkan dengan total Rp.{total_harga_produk}')
        print()
        print(f'Total harga sementara: Rp.{total_harga}')
       
        tambah_produk = input("Apakah anda ingin menambah produk? [y/n]: ").lower()
        bersihkan_layar()
        while tambah_produk not in ['y','n']:
            tambah_produk = input("Apakah anda ingin menambah produk? [y/n]: ").lower()
            print()
            print("Input tidak valid. Silakan masukkan 'y' atau 'n' saja.")
            print()
        if tambah_produk=="n":
            break
    
    global poin_user 
    print("\nRingkasan Pembelian:")
    print("=" * 30)
    print(f'Total Produk: {total_produk}')
    print(f"Total Harga: Rp.{total_harga}")
    print(f"Poin Anda: {poin_user}")
    print("=" * 30)
    
    if poin_user > 0:
        tukar_poin = input('Apakah anda ingin menukar poin anda? [y/n]: ')
        print()
        if tukar_poin == 'y':
            nilai_tukar = poin_user*nilai_poin
            if nilai_tukar >= total_harga:
                poin_terpakai = total_harga // nilai_poin
                poin_user -= poin_terpakai
                simpan_poin(poin_user)
                print(f"Transaksi berhasil ditukar dengan {poin_terpakai} poin.")
                print("Tidak ada yang harus dibayar")
                print()
                print(input("Tekan enter untuk melanjutkan..."))
            else: 
                sisa_bayar = total_harga - nilai_tukar
                poin_terpakai = poin_user
                poin_user = 0
                simpan_poin(poin_user)
                print(f'Anda menggunakan {poin_terpakai} poin dan mendapatkan potongan harga senilai Rp.{nilai_tukar}')
                print(f'Sisa yang harus anda bayar: Rp.{sisa_bayar}')
                print()
                print(input("Tekan enter untuk melanjutkan..."))
                bersihkan_layar()
        else:
            print(f'Total yang harus anda bayar adalah Rp.{total_harga}') 
            print()
            print(input("Tekan enter untuk melanjutkan..."))
            bersihkan_layar()
            
    else:
        print(f'Total yang harus anda bayar: Rp.{total_harga}')
        print()
        print(input("Tekan enter untuk melanjutkan..."))
        bersihkan_layar()
    menu_pembeli()

def tukar_limbah():
    global poin_user 
    while True:
        result = pyfiglet.figlet_format("Tukar Limbah")
        print(result)
        try:
            limbah = pd.read_csv("limbah.csv")
        except FileNotFoundError:
            print('File tidak ditemukan')
            return
        teks = "Daftar Limbah"
        print('='*30)
        print(f"{teks:^30}")
        print('='*30)
        print(tabulate(limbah, headers='keys', tablefmt='fancy_grid', showindex=False))

        try:
            print()
            pilih_limbah = int(input('Masukkan ID limbah yang ingin anda tukar: '))
            if pilih_limbah not in [i for i in limbah['ID']]:
                print(f'ID {pilih_limbah} tidak ditemukan. Silakan coba kembali')
                continue
        
            berat = float(input('Masukkan berat limbah (kg): '))  
            if berat <= 0:
                print("Berat limbah harus lebih dari 0")
                continue
        except ValueError:
            print()
            print('Input harus berupa angka, Silakan coba kembali')
            menu_pembeli()
            
        poin_limbah = limbah.loc[limbah['ID'] == pilih_limbah, 'Poin/kg'].iloc[0]
        jenis_limbah = limbah.loc[limbah['ID'] == pilih_limbah, 'Jenis Limbah'].iloc[0]
        
        total_poin_limbah = int(poin_limbah*berat)
        poin_user += total_poin_limbah
        simpan_poin(poin_user)
        
        print(f'Anda ingin menukar {jenis_limbah} dengan berat {berat} kg dan akan mendapatkan poin sebanyak {total_poin_limbah}')
        print()
        print(f'Total poin saat ini: {poin_user}')
       
        tambah_limbah = input("Apakah anda ingin menukar limbah lagi? [y/n]: ").lower()
        
        while tambah_limbah not in ['y','n']:
            tambah_limbah = input("Apakah anda ingin menukar limbah lagi? [y/n]: ").lower()
            print()
            print("Input tidak valid. Silakan masukkan 'y' atau 'n' saja.")
        print()
        if tambah_limbah =="n":
            print(f'{poin_user} poin telah ditambahkan')
            print(input('Tekan enter untuk melanjutkan...'))
            break
    menu_pembeli()
    
        
def menu_pembeli():
    result = pyfiglet.figlet_format("Menu Pembeli")
    print(result)
    global poin_user
    poin_user = baca_poin()
    while True:
        print('1.Checkout')
        print('2.Tukar Limbah')
        print('3.Kembali ke login')
        
        choice = input("\nAnda ingin ke menu apa? (1/2/3): ")
        bersihkan_layar()
        
        if choice == '1':
            poin_user = checkout()
            break
        elif choice == '2':
            poin_user = tukar_limbah()
            break
        elif choice == '3':
            login()
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi")
            input('Tekan enter untuk melanjutkan...')
            
def daftar_produk():
     while True:
        result = pyfiglet.figlet_format("Daftar Produk")
        print(result)
        try:
            produk = pd.read_csv('produk.csv')
        except FileNotFoundError:
            print('File tidak ditemukan')
            return
        print(tabulate(produk, headers='keys', tablefmt='fancy_grid', showindex=False))
        
        input("\nTekan enter untuk melanjutkan...")
        break

def tambah_produk():    # tanpa modul csv
    result = pyfiglet.figlet_format("Tambah Produk")
    print(result)

    # Cek apakah file produk.csv sudah ada
    try:
        with open('produk.csv', mode='r') as file:
            lines = file.readlines()  # Membaca semua baris dalam file
    except FileNotFoundError:
        # Jika file tidak ditemukan, mulai dengan header
        lines = ["ID,Nama Barang,Harga Barang (Rp)\n"]
        
    teks = "Daftar Produk"
    print()
    print("="*30)
    print(f"{teks:^30}")
    print("="*30)
    
    data = [line.strip().split(',') for line in lines]
    print(tabulate(data[1:], headers=data[0], tablefmt='fancy_grid', showindex=False))

    # Cek apakah file memiliki data atau hanya header
    if len(lines) > 1:
        # Ambil ID terakhir dari baris terakhir
        last_line = lines[-1].strip().split(",")
        id_terakhir = int(last_line[0])  # Ambil ID terakhir
        id_barang = str(id_terakhir + 1)
    else:
        id_barang = '1'  # Jika hanya header, ID dimulai dari 1

    # Input data baru
    nama = input("\nMasukkan nama barang: ")
    harga = input("Masukkan harga barang (angka): ")
    bersihkan_layar()

    # Validasi input harga
    if not harga.isdigit():
        print("Harga harus berupa angka!")
        return

    # Buat baris baru untuk ditambahkan
    baris_baru = f"{id_barang},{nama},{harga}\n"

    # Tambahkan baris ke file
    with open('produk.csv', mode='a', encoding='utf-8') as file:
        file.write(baris_baru)

    print(f"Barang dengan ID {id_barang} berhasil ditambahkan!")
    input("Tekan enter untuk melanjutkan...")
    menu_admin()
    
def ubah_produk():
    result = pyfiglet.figlet_format("Ubah Produk")
    print(result)
    barang = []
    try:
        with open('produk.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                barang.append(row)
        # with open('produk.csv','r') as file:
        #     lines = file.readlines()
    except FileNotFoundError:
        print('File produk tidak ditemukan. Pastikan file sudah ada')
        return
    
    teks = "Daftar Produk"
    print()
    print("="*30)
    print(f"{teks:^30}")
    print("="*30)
    print()
    print(tabulate(barang, headers='keys', tablefmt='fancy_grid', showindex=False))
    
    id_ubah = input("\nMasukkan ID barang yang ingin diubah: ")
    
    
    id_found = False
    
    for data in barang:
        if data['ID'] == id_ubah:
            id_found = True
            data['Nama Barang'] = input("Masukkan nama barang baru: ")
            harga_baru = input("Masukkan harga barang baru: ")
            if not harga_baru.isdigit():
                print("Harga harus berupa angka!")
                return
            data['Harga Barang (Rp)'] = harga_baru
            break
    
        elif not id_found:
            print("ID tidak valid, cek daftar barang terlebih dahulu.")
        else:        
            with open('produk.csv', 'w', newline='') as csv_file:
                fieldnames = ['ID', 'Nama Barang', 'Harga Barang (Rp)']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(barang)
            print(f"Barang dengan ID {id_ubah} berhasil diubah!")
            input("Tekan enter untuk melanjutkan...")
        menu_admin()
        
def hapus_produk():
    result = pyfiglet.figlet_format("Hapus Produk")
    print(result)
    
    try:
        with open('produk.csv','r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('File produk tidak ditemukan. Pastikan file sudah ada')
        return
    
    teks = "Daftar Produk"
    print()
    print("="*30)
    print(f"{teks:^30}")
    print("="*30)
    print()
    
    data = [line.strip().split(',') for line in lines]
    print(tabulate(data[1:], headers=data[0], tablefmt='fancy_grid', showindex=False))
    
    id_hapus = input("\nMasukkan ID barang yang ingin dihapus: ")
    try: 
        with open('produk.csv', mode='r') as produk:
                reader = csv.DictReader(produk)
                data = list(reader)
    
        produk_hapus = [item for item in data if item['ID'] != id_hapus]
        
        if len(produk_hapus) == len(data):
            print(f"Barang dengan ID {id_hapus} tidak ditemukan")
            menu_admin()
            return
        
        with open('produk.csv', mode='w', newline='') as produk:
            fieldnames = ['ID', 'Nama Barang', 'Harga Barang (Rp)']
            writer = csv.DictWriter(produk, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(produk_hapus)
        
        print(f"Barang dengan ID {id_hapus} berhasil dihapus")
    except FileNotFoundError:
        print("File produk tidak ditemukan")

def menu_admin():
    while True:
        result = pyfiglet.figlet_format("Menu Admin")
        print(result)
        print("1. Lihat Daftar Produk")
        print("2. Tambah Produk")
        print("3. Ubah Produk")
        print("4. Hapus Produk")
        print("5. Kembali ke Login")
        pilihan = input("Pilih menu: ")
        bersihkan_layar()
        if pilihan == '1':
            daftar_produk()
            bersihkan_layar()
        elif pilihan == '2':
            tambah_produk()
        elif pilihan == '3':
            ubah_produk()
            bersihkan_layar()
        elif pilihan == '4':
            hapus_produk()
            bersihkan_layar()
        elif pilihan == '5':
            login()
        else:
            print("Pilihan tidak valid!")
login()             
        

    




