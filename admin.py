import pandas as pd
import csv

def daftar_barang():
    try:
        with open('produk.csv', mode='r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

            if not data:
                print("\nTidak ada produk dalam daftar.")
                return

            teks = "Daftar Barang"
            print('=' * 30)
            print(f"{teks:^30}")
            print('=' * 30)
            print(f"{'ID':<5} {'Nama Barang':<20} {'Harga Barang (Rp)':<10}")
            print("-" * 45)
            for item in data:
                print(f"{item['ID']:<5} {item['Nama Barang']:<20} {item['Harga Barang (Rp)']:<10}")
    except FileNotFoundError:
        print("\nFile produk.csv tidak ditemukan. Tambahkan barang terlebih dahulu.")

def tambah_barang():
    teks = "Tambah Barang"
    print('=' * 30)
    print(f"{teks:^30}")
    print('=' * 30)
    try:        
        with open('produk.csv', mode='r') as file:
            reader = csv.DictReader(file)
            produk = list(reader)
        
        if produk:
            id_terakhir = max(int(item['ID']) for item in produk)
            id_barang = str(id_terakhir + 1)
        else:
            id_barang = '1'
    except FileNotFoundError:
        
        produk = []
        id_barang = '1'

    nama = input("Masukkan nama barang: ")
    harga = input("Masukkan harga barang: ")
    
    if not harga.isdigit():
        print("Harga harus berupa angka!")
        return
    
    produk_baru = {
        'ID': id_barang,
        'Nama Barang': nama,
        'Harga Barang (Rp)': harga
    }
    produk.append(produk_baru)

    with open('produk.csv', mode='w', newline='') as file:
        fieldnames = ['ID', 'Nama Barang', 'Harga Barang (Rp)']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(produk)

    print(f"Barang dengan ID {id_barang} berhasil ditambahkan!")

def ubah_produk():
    result = pyfiglet.figlet_format("Ubah Produk")
    print(result)
    barang = []
    
    try:
        with open('produk.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                barang.append(row)
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
            
            while True:
                harga_baru = input("Masukkan harga barang baru: ")
                if harga_baru.isdigit():
                    data['Harga Barang (Rp)'] = harga_baru
                    break
                else:
                    print("Harga harus berupa angka! Silakan coba lagi.")
            break
    
    if not id_found:
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
    
def hapus_barang():
    teks = "Hapus Barang"
    print('=' * 30)
    print(f"{teks:^30}")
    print('=' * 30)
    id_hapus = input("Masukkan ID barang yang ingin dihapus: ")
    
    with open('produk.csv', mode='r') as produk:
        reader = csv.DictReader(produk)
        data = list(reader)
    
    produk_hapus = [item for item in data if item['ID'] != id_hapus]
    
    if len(produk_hapus) == len(data):
        print("Barang tidak ditemukan")
        return
    
    for index, item in enumerate(produk_hapus):
        item['ID'] = str(index + 1)
    
    with open('produk.csv', mode='w', newline='') as produk:
        fieldnames = ['ID', 'Nama Barang', 'Harga Barang (Rp)']
        writer = csv.DictWriter(produk, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(produk_hapus)
    
    print(f"Barang dengan ID {id_hapus} berhasil dihapus")

def menu_admin():
    while True:
        teks = "Menu Admin"
        print('=' * 30)
        print(f"{teks:^30}")
        print('=' * 30)
        print("1. Lihat Daftar Barang")
        print("2. Tambah Barang")
        print("3. Ubah Barang")
        print("4. Hapus Barang")
        print("5. Kembali ke Login")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            daftar_barang()
        elif pilihan == '2':
            tambah_barang()
        elif pilihan == '3':
            ubah_barang()
        elif pilihan == '4':
            hapus_barang()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid!")
