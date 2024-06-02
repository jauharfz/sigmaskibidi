import time
import sys

users = {}
logged_in_user = False 
sell_history = {}
buy_history = {}
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
        username = input("Masukan username(Enter untuk kembali): ")
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
        username = input("Masukan username(Enter untuk kembali): ")
        if username == '':
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
        if attempts == 3:
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
            main_menu()
        else:
            print("Masukan pilihan yang valid")

def sell_account():
    while True:
        print("Jual akun\nPilih kategori game")
        for idx, game in enumerate(games, 1):
            print(f"{idx}. {game}")
        print("0. Kembali")
        choice = input("Masukan pilihan: ")
        if choice == '0':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(games):
            game_choice = games[int(choice) - 1]
            judul = input("Masukan judul: ")
            deskripsi = input("Masukan deskripsi: ")
            while True:
                harga = input("Masukan harga: ")
                if harga.isdigit():
                    break
                print("Mohon masukan harga berupa angka")
            email = input("Masukan email: ")
            while True:
                password = input("Masukan password: ")
                if len(password) >= 6:
                    break
                print("Password minimal 6 karakter")
            accounts = {
                'title': judul,
                'description': deskripsi,
                'price': int(harga),
                'email': email,
                'password': password,
                'owner': logged_in_user,
                'sold': False
            }
            account_in_game[game_choice].append(accounts)
            sell_history.setdefault(logged_in_user, []).append(accounts)
            input("Akun berhasil ditambahkan di daftar jual")
            break
        else:
            print("Pilihan tidak valid")
              
def buy_account():
    while True:
        print("Beli akun\nPilih kategori game")
        for idx, game in enumerate(games, 1):
            print(f"{idx}. {game}")
        print("0. Kembali")
        choice = input("Masukan pilihan: ")
        if choice == '0':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(games):
            game_choice = games[int(choice) - 1]
            available_accounts = [acc for acc in account_in_game[game_choice] if acc['owner'] != logged_in_user and not acc['sold']]
            if available_accounts:
                for idx, avl in enumerate(available_accounts, 1):
                    print(f"{idx}. {avl['title']}, Harga= {avl['price']}")
                print("0. Kembali")
                choice2 = input("Masukan pilihan: ")
                if choice2 == '0':
                    break
                elif choice2.isdigit() and 1 <= int(choice2) <= len(available_accounts):
                    selected_acc = available_accounts[int(choice2)-1]
                    print(f"Judul: {selected_acc['title']}\n"
                          f"Deskripsi: {selected_acc['description']}\n"
                          f"Harga: {selected_acc['price']}\n"
                          f"1. Beli\n"
                          f"0. Kembali")
                    choice3 = input("Masukan pilihan: ")
                    if choice3 == '0':
                        continue
                    elif choice3 == '1':
                        purchase_acc(selected_acc)
                    else:
                        print("Masukan pilihan yang valid")
                else:
                    print("Masukan pilihan yang valid")
            else:
                input("Akun tidak tersedia, tekan enter untuk kembali")
        else:
            print("Masukan tidak valid")
              
def purchase_acc(selected_acc):
    while True:
        print("Pilih metode pembayaran:")
        print("1. OVO")
        print("2. DANA")
        print("3. GoPay")
        print("4. Kembali")
        choice = input("Pilih metode pembayaran: ")

        if choice in ['1', '2', '3']:
            while True:
                phone_number = input("Masukkan nomor HP: ")
                if phone_number.isdigit():
                    break
                print("Nomor HP harus berupa angka.")

            print("Mengirim OTP...")
            time.sleep(5)
            otp = input("Masukkan OTP: ")
            print("1. Konfirmasi Pembelian")
            print("2. Batalkan Pembelian")
            confirm = input("Pilih menu: ")

            if confirm == '1':
                selected_acc["sold"] = True
                buy_history.setdefault(logged_in_user, []).append(selected_acc)
                input("Pembelian berhasil. Email dan password bisa dilihat di riwayat pembelian.")
                break
            elif confirm == '2':
                continue
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

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
            user_menu()
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
                print(f"Email: {selected_item['email']}")
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
                    print(f"Email: {selected_item['email']}")
                    print(f"Password: {selected_item['password']}")
                    sale_detail_menu(selected_item, editable = True)
                else:
                    selected_item = sold_sales[choice - len(unsold_sales) - 1]
                    print(f"Judul: {selected_item['title']}")
                    print(f"Deskripsi: {selected_item['description']}")
                    print(f"Harga: {selected_item['price']}")
                    print(f"Email: {selected_item['email']}")
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
            return
        elif choice == '2' and editable:
            edit_sale(account)
        elif choice == '0' and not editable or choice == '3' and editable:
            break
        else:
            print("masukan pilihan yang valdef account_settings():
                  
def delete_sale(account):
    while True:
        print("Hapus akun")
        confirm = input("Ketik 'ya' jika akun ingin dihapus: ")
        if confirm == 'ya':
            for game in games:
                if account in account_in_game[game]:
                    account_in_game[game].remove(account)
            sell_history[logged_in_user].remove(account)
            print("Akun berhasil dihapus")
            break
        else:
            print("Akun gagal dihapus")
            break
            
def edit_sale(account):
    while True:
        print("Edit akun\n"
              "1. Judul\n"
              "2. Deskripsi\n"
              "3. Harga\n"
              "4. Email\n"
              "5. Password\n"
              "6. Kembali")
        choice = input("Pilih menu: ")
        if choice == '1':
            judul = input("Masukan judul baru: ")
            account['title'] = judul
            print("Judul berhasil diubah")
        elif choice == '2':
            deskripsi = input("Masukan deskripsi baru: ")
            account['description'] = deskripsi
            print("Deskripsi berhasil diubah")
        elif choice == '3':
            while True:
                price = input("Masukan harga baru: ")
                if price.isdigit():
                    account['price'] = int(price)
                    print("Harga berhasil diubah")
                    break
                else:
                    print("Harus menggunakan angka")
        elif choice == '4':
            email = input("Masukan email baru: ")
            account['email'] = email
            print("Email berhasil diubah")
        elif choice == '5':
            while True:
                password = input("Masukan password baru (minimal 6 karakter): ")
                if len(password) >= 6:
                    account['password'] = password
                    print("Password berhasil diubah")
                    break
                else:
                    print("Password minimal 6 karakter")
        elif choice == '6':
            break
        else:
            print("Masukan pilihan yang benar")

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


def change_password():
    while True:
        old_pwd = input("masukan password lama(tekan Enter untuk kembali)")
        if old_pwd == '':
            break
        if old_pwd != users[logged_in_user]['password']:
            print("password tidak valid")
            continue
        new_pwd = input("masukan password baru: ")
        if len(new_pwd) < 6:
            print("password minimal 6 karakter")
            continue

        users[logged_in_user]['password'] = new_pwd
        input("password telah berhasil diubah")
        break            

def change_username():
    global logged_in_user
    while True:
        old_user = input("masukan username lama(atau tekan Enter untuk kembali): ")
        if old_user == '':
            break
        if old_user != logged_in_user:
            print("username tidak valid")
            continue
        new_user = input("masukan username baru: ")
        if not new_user.isalnum():
            print("harus menggunakan huruf atau angka saja")
            continue
        if new_user in users:
            print("username telah digunakan")
            continue
        users[new_user] = users.pop(logged_in_user)
        users[new_user]['username'] = new_user
        if logged_in_user in buy_history:
            buy_history[new_user] = buy_history.pop(logged_in_user)
        if logged_in_user in sell_history:
            sell_history[new_user] = sell_history.pop(logged_in_user)
        for game, accounts in account_in_game.items():
            for account in accounts:
                if account['owner'] == logged_in_user:
                    account['owner'] = logged_in_user

        logged_in_user = new_user
        input("username berhasil berubah")
        break

def delete_account():
    global logged_in_user
    while True:
        username = input("masukan username(tekan Enter untuk kembali): ")
        if username == '':
            break
        password = input("masukan password: ")
        if username == users[logged_in_user]['username'] and password == users[logged_in_user]['password']:
            confirm = input("ketik 'ya' untuk menghapus akun: ")
            if confirm == 'ya':
                for game in games:
                    account_in_game[game] = [acc for acc in account_in_game[game] if acc['owner'] != logged_in_user]
                del users[logged_in_user]
                buy_history.pop(logged_in_user, None)
                sell_history.pop(logged_in_user, None)
                logged_in_user = None
                input("akun berhasil dihapus")
                main_menu()
                return
            else:
                print("akun gagal dihapus")
                continue
        else:
            print("username atau password tidak valid")
            continue


if __name__ == "__main__":
    main_menu()
