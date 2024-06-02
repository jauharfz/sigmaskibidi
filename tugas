import time

users = {}
logged_in_user = False 
games = ["Legenda Seluler", "EpEp", "King Bengsin"]
account_in_game = {for game in games: []}

def main_menu():
      print("Ini bagian Login/Register\n"
            "1. Register\n"
            "2. Login\n"
            "3. Keluar dari program")
      choice = input("Pilih Menu: ")
      if choice == '1':
           register()
      elif choice == '2':
          login()
      elif choice == '3':
          print("Selamat anda telah keluar :)")
          sys.exit
      else:
          print("masukan input yang valid")

def register():
    while True:
        print("Registrasi:")
        username = input("Masukan username(0 untuk kembali): ")
        if username == '0':
            break
        if not username.isalnum():
            print("Username harus huruf ataupun angka")
            continue
        if username in users:
            print("Username sudah digunakan")
            continue
        password = input("Masukan password(minimal 6 karakter): ")
        if len(password) < 6:
            print("Karakter passwordnya kurang :(")
            continue
        name = input("Masukan nickname(bebas): ")
        users[username] = {"name": name, "password": password, "username": username}
        print(f"Berbahagialah nama anda: {name} sudah terdaftar")
        break

def login():
    global logged_in_user
    while True:
        print("Halaman login")
        username = input("Masukan username(0 untuk kembali): ")
        if username == '0':
            break
        if username not in users:
            print("Mohon masukan username yang benar")
            continue

        attempts = 0
        while attempts < 3:
            password = input("Masukan password: ")
            if password == users[username]["password"]:
                logged_in_user = username
                print(f"Selamat datang {users[username]['name']}")
                user_menu()
                return
            else:
                attempts += 1
                print(f"Password salah({attempts}/3)")
        if attempts >= 3:
            print("Silahkan kembali masukan username")
            continue

def user_menu():
    global logged_in_user
    while True:
        print("Menu Utama\n"
              "1. Lihat profil\n"
              "2. Jual akun\n"
              "3. Beli akun\n"
              "4. Log out")
        choice = input("Pilih menu: ")
        if choice == '1':
            view_profile()
        elif choice == '2':
            sell_account()
        elif choice == '3':
            buy_account()
        elif choice == '4':
            logged_in_user = None
            break
        else:
            print("Masukan pilihan yang valid")

def view_profile():
    while True:
        print("Lihat profil\n"
              "1. Riwayat pembelian & penjualan akun\n"
              "2. Pengaturan akun\n"
              "3. Kembali ke menu")
        choice = input("Pilih menu: ")
        if choice == '1':
            view_history()
        elif choice == '2':
            account_settings()
        elif choice == '3':
            break
        else:
            print("Mohon masukan pilihan yang valid")

def view_history():
    while True:
        print("Riwayat pembelian & penjualan akun:\n"
              "1. Riwayat pembelian\n"
              "2. Riwayat penjualan\n"
              "3. Keluar")
        choice = input("Pilih menu: ")
        if choice == '1':
            view_purchase_history()
        elif choice == '2':
            view_sale_history()
        elif choice == '3':
            view_profile()
        elif:
            print("masukan pilihan yang valid")

def view_purchase_history():
    while True:
        print("Histori Pembelian")
        purchases = buy_history.get(logged_in_user, [])
        if purchases:
            for idx, lst in enumerate(purchases, 1):
                print(f"{idx}. {lst['title']}")
            print("0. Kembali")
            choice = input("Pilih akun: ")
            if choice == '0'
                break
            if choice.isdigit() and 1 <= int(choice) <= len(purchases):
                selected_item = purchases[int(choice)-1]
                print(f"Judul: {selected_item['title']}")
                print(f"Deskripsi: {selected_item['description']}")
                print(f"Harga: {selected_item['price']}")
                print(f"ID: {selected_item['id']}")
                print(f"Password: {selected_item['password']}")
                input("Tekan Enter untuk kembali.")
            else:
                print("masukan pilihan yang valid")
        else:
            input("belum ada akun yang dibeli, tekan enter untuk kembali")
            break
