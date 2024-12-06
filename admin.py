def daftar_produk():
     while True:
        result = pyfiglet.figlet_format("Daftar Produk")
        print(result)
        try:
            produk = pd.read_csv('produk.csv', on_bad_lines='skip')
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

    # cek apakah file memiliki data atau hanya header
    if len(lines) > 1:
        # ambil ID terakhir dari baris terakhir
        last_line = lines[-1].strip().split(",")
        id_terakhir = int(last_line[0])  # Ambil ID terakhir
        id_barang = str(id_terakhir + 1)
    else:
        id_barang = '1'  # jika hanya header, ID dimulai dari 1

    # input data produk
    nama = input("\nMasukkan nama barang: ")
    while not nama:
        print("Nama barang tidak boleh kosong!")
        nama = input("\nMasukkan nama barang: ")
        
    harga = input("Masukkan harga barang (angka): ")
    while not harga.isdigit():
        print("Harga harus berupa angka!")
        harga = input("Masukkan harga barang (angka): ")
    bersihkan_layar()

    # Buat baris baru untuk ditambahkan
    baris_baru = f"{id_barang},{nama},{harga}\n"

    try:
        with open('produk.csv', mode='a', encoding='utf-8') as file:
            file.write(baris_baru)
    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan produk: {e}")
        return

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
            nama_baru = input("Masukkan nama barang baru: ")
            # validasi nama
            if not nama_baru:
                print("Nama barang tidak boleh kosong!")
                return
            data['Nama Barang'] = nama_baru
            # validasi harga
            harga_baru = input("Masukkan harga barang baru: ")
            if not harga_baru.isdigit():
                print("Harga harus berupa angka!")
                return
            data['Harga Barang (Rp)'] = harga_baru
            break
    
    if not id_found:
        print("ID tidak valid, cek daftar barang terlebih dahulu.")
        return
    
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
        
        for index, item in enumerate(produk_hapus):
            item['ID'] = str(index + 1)
        
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