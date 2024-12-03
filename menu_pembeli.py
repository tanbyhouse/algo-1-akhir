import pandas as pd 
    
    #Variabel global
poin_user = 0   
nilai_poin = 500 #Nilai 1 poin dalam rupiah

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
    total_harga = 0 
    
    while True:
        try:
            produk = pd.read_csv('produk.csv')
        except FileNotFoundError:
            print('File tidak ditemukan')
            return
        
        print()
        print("="*30)
        print("        Daftar Produk    ")
        print("="*30)
        print()
        print(produk.to_string(index=False))
        print()
        
        try:
            pilih_produk = int(input('Masukkan ID produk yang ingin anda beli: '))-1
            if pilih_produk not in produk['ID']:
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
            
        total_harga_produk = int(harga_produk*jumlah)
        total_harga += total_harga_produk
        
        print()
        print(f'{nama_produk} ditambahkan sebanyak {jumlah} dengan total Rp.{total_harga_produk}')
        print()
        print(f'Total harga sementara: Rp.{total_harga}')
       
        tambah_produk = input("Apakah anda ingin menambah produk? [y/n]: ").lower()
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
        else:
            print(f'Total yang harus anda bayar adalah Rp.{total_harga}') 
            print()
            print(input("Tekan enter untuk melanjutkan..."))
            
    else:
        print(f'Total yang harus anda bayar: Rp.{total_harga}')
        print()
        print(input("Tekan enter untuk melanjutkan..."))
    menu_pembeli()

def tukar_limbah():
    global poin_user 
    while True:
        try:
            limbah = pd.read_csv("limbah.csv")
        except FileNotFoundError:
            print('File tidak ditemukan')
            return
        
        print()
        print('='*30)
        print('        Daftar Limbah     ')
        print('='*30)
        print()
        print(limbah.to_string(index=False))

        try:
            pilih_limbah = int(input('Masukkan ID limbah yang ingin anda tukar: '))-1
            if pilih_limbah not in limbah['ID']:
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
    
    
def keluar():
    print('Terima kasih telah menggunakan sistem kami')
    
def menu_pembeli():
    global poin_user
    poin_user = baca_poin()
    while True:
        print()
        print('='*30)
        print('         Menu Pembeli    ')
        print('='*30)
        print('1.Checkout')
        print('2.Tukar Limbah')
        print('3.Keluar')
        print()
        
        choice = input("Anda ingin ke menu apa? (1/2/3): ")
        print()
        
        if choice == '1':
            poin_user = checkout()
            break
        elif choice == '2':
            poin_user = tukar_limbah()
            break
        elif choice == '3':
            keluar()
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi")
menu_pembeli()

