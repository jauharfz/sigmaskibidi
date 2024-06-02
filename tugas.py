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
        else:
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
            if choice == '0':
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

def view_sale_history():
    while True:
        print("Histori penjualam")
        sales = sell_history.get(logged_in_user, [])
        unsold_sales = [item for item in sales if not item['sold']]
        sold_sales = [item for item in sales if item['sold']]
        if unsold_sales or sold_sales:
            if unsold_sales:
                print("akun yang belum terjual")
                for idx, item in enumerate(unsold_sales, 1):
                    print(f"{idx}. {item['title']}")
            else:
                print("belum ada akun yang belum terjual")
                  
            if sold_sales:
                print("akun yang sudah terjual")
                for idx, item in enumerate(sold_sales, 1):
                    print(f"{idx+len(unsold_sales)}. {item['title']}")
            else:
                print("belum ada akun yang sudah terjual")
        else:
            input("belum ada riwayat penjualan, tekan enter untuk kembali")
            view_history()
        print("0. Kembali")
          
        choice = input("masukan pilihan: ")
        if choice == '0':
            break
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(unsold_sales) + len(sold_sales):
                if choice <= len(unsold_sales):
                    selected_item = unsold_sales[choice - 1]
                    print(f"Judul: {selected_item['title']}")
                    print(f"Deskripsi: {selected_item['description']}")
                    print(f"Harga: {selected_item['price']}")
                    print(f"ID: {selected_item['id']}")
                    print(f"Password: {selected_item['password']}")
                    sale_detail_menu(selected_item, editable = True)
                else:
                    selected_item = sold_sales[choice - len(unsold_sales) - 1]
                    print(f"Judul: {selected_item['title']}")
                    print(f"Deskripsi: {selected_item['description']}")
                    print(f"Harga: {selected_item['price']}")
                    print(f"ID: {selected_item['id']}")
                    print(f"Password: {selected_item['password']}")
                    sale_detail_menu(selected_item, editable = False)
            else:
                print("masukan pilihan yang valid")
        else:
            print("masukan pilihan yang valid")

def sale_detail_menu(account, editable):
    while True:
        if editable:
            print("1. Hapus\n"
                  "2. Edit\n"
                  "3. Kembali")
        else:
            print("0. Kembali")
        choice = input("Pilih menu: ")
        if choice == '1' and editable:
            delete_sale(account)
        elif choice == '2' and editable:
            edit_sale(account)
        elif choice == '0' and not editable or choice == '3' and editable:
            break
        else:
            print("masukan pilihan yang valdef account_settings():

def account_settings():
    while True:
        print("Pengaturan akun\n"
                "1. Ubah Password\n"
                "2. Ubah Username\n"
                "3. Hapus Akun\n"
                "4. Kembali\n")
        choice = input("Pilih menu: ")

        if choice == '1':
            change_password()
        elif choice == '2':
            change_username()
        elif choice == '3':
            delete_account()
            break
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
