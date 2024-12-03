from admin import menu_admin

def login():
    while True:
        print("\n--- Login ---")
        print("1. Admin")
        print("2. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            menu_admin()  # Memanggil menu_admin() dari admin.py
        elif pilihan == '2':
            print("Terima kasih telah menggunakan program!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    login()  # Memulai login() saat program dijalankan
