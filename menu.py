import os
import subprocess
import shutil
from colorama import Fore, init

# Inisialisasi colorama
init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_intro_border():
    border = "╭" + "─" * 48 + "╮"
    intro_text = " " * 10 + "SELAMAT DATANG DI MENU" + " " * 10
    intro_line = "│" + intro_text + " " * (48 - len(intro_text) - 0) + "│"
    
    print(Fore.YELLOW + border)
    print(Fore.YELLOW + intro_line)
    print(Fore.YELLOW + border)

def display_menu_border():
    border = "├" + "─" * 48 + "┤"
    print(Fore.CYAN + border)

def main_menu():
    clear()
    display_intro_border()
    display_menu_border()
    
    print(Fore.CYAN + "│" + Fore.GREEN + " 1. Payco" + " " * 40 + "")
    print(Fore.CYAN + "│" + Fore.GREEN + " 2. Reset" + " " * 40 + "")
    print(Fore.CYAN + "│" + Fore.GREEN + " 3. Access email" + " " * 10 + "")
    print(Fore.CYAN + "│" + Fore.GREEN + " 4. Access admin" + " " * 0 + "")
    print(Fore.CYAN + "│" + Fore.RED + " 0. Keluar" + " " * 0 + "")
    display_menu_border()
    print(Fore.CYAN + "│" + " " * 48 + "│")
    print(Fore.CYAN + "╰" + "─" * 48 + "╯")

def open_script(choice):
    clear()
    if choice == '1':
        if not os.path.exists("src/run.py"):
            print(Fore.RED + "Anda bukanlah admin! Beli bot ini untuk mengakses penuh.")
            return
        
        os.system("python src/run.py")

        local_result_path = 'result.txt'
        sdcard_result_path = '/sdcard/result.txt'

        if os.path.exists(sdcard_result_path):
            print(Fore.GREEN + "═══════════════════════════════════") 
            if os.path.exists(local_result_path):
                # Membaca isi dari result.txt di direktori saat ini
                with open(local_result_path, 'r') as local_file:
                    local_content = local_file.read()
                
                # Menambahkan isi dari result.txt di direktori saat ini ke yang ada di /sdcard/
                with open(sdcard_result_path, 'a') as sd_file:
                    sd_file.write(local_content)
                print(Fore.YELLOW + " ")
                
                # Menghapus result.txt dari direktori saat ini setelah memindahkan isinya
                os.remove(local_result_path)
                print(Fore.YELLOW + "Berhasil Membuat akun & Memverifikasi email, Akun Payco anda telah berhasil di simpan di Internal Storage")
            else:
                print(Fore.RED + "File result.txt tidak ditemukan di direktori saat ini.")
        else:
            if os.path.exists(local_result_path):
                try:
                    shutil.move(local_result_path, sdcard_result_path)
                    print(Fore.YELLOW + "Berhasil Membuat akun & Memverifikasi email, Akun Payco anda telah berhasil di simpan di Internal Storage")
                except Exception as e:
                    print(Fore.RED + f"Gagal memindahkan file: {e}")
            else:
                print(Fore.RED + "File result.txt tidak ditemukan di direktori saat ini.")

    elif choice == '2':
        if not os.path.exists("reset.py"):
            print(Fore.RED + "Anda bukanlah admin! Beli bot ini untuk mengakses penuh.")
            return
        os.system("python reset.py")
    elif choice == '3':
        print(Fore.CYAN + "Membuka https://m.kuku.lu/id.php di browser...")
        subprocess.run(["xdg-open", "https://m.kuku.lu/id.php"]) if os.name != 'nt' else subprocess.run(["start", "https://m.kuku.lu/id.php"], shell=True)
    elif choice == '4':
        if not os.path.exists("admin.py"):
            print(Fore.RED + "Anda bukanlah admin! Beli bot ini untuk mengakses penuh.")
            return
        os.system("python admin.py")
    elif choice == '0':
        print(Fore.YELLOW + "Keluar dari program.")

def return_to_menu():
    while True:
        back = input(Fore.CYAN + "Apakah Anda ingin kembali ke menu utama? (y/n): ").lower()
        if back == 'y':
            return True
        elif back == 'n':
            print(Fore.YELLOW + "Menutup konsol. Terima kasih!")
            return False
        else:
            print(Fore.RED + "Kesalahan: Masukkan 'y' untuk kembali ke menu atau 'n' untuk menutup konsol.")

def main():
    while True:
        main_menu()
        choice = input(Fore.CYAN + "Masukkan pilihan Anda: ")
        
        if choice in {'0', '1', '2', '3', '4'}:
            if choice == '0':
                print(Fore.YELLOW + "Keluar dari program.")
                break
            open_script(choice)
            if not return_to_menu():
                break
        else:
            print(Fore.RED + "Kesalahan: Masukkan pilihan yang benar antara 0 hingga 4.")
            if not return_to_menu():
                break

if __name__ == "__main__":
    main()
