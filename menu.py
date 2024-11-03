import os
import subprocess
import shutil  # Import shutil untuk memindahkan file
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def clear():
    # Membersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    border = "=" * 40  # Baris untuk membingkai logo
    logo = """
  
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
████╗░████║██╔════╝████╗░██║██║░░░██║
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
    by @forumkt
    """
    print(Fore.YELLOW + border)
    print(Fore.YELLOW + logo)
    print(Fore.YELLOW + border)

def main_menu():
    clear()
    display_logo()
    border = "=" * 40  # Baris untuk membingkai menu
    print(Fore.CYAN + border)
    print(Fore.CYAN + Style.BRIGHT + "Pilih Menu:")
    print(Fore.GREEN + "1. Payco")
    print(Fore.GREEN + "2. Reset")
    print(Fore.GREEN + "3. Access email")
    print(Fore.GREEN + "4. Access admin")
    print(Fore.RED + "0. Keluar")
    print(Fore.CYAN + border)

def open_script(choice):
    clear()
    if choice == '1':
        if not os.path.exists("src/run.py"):
            print(Fore.RED + "Anda bukanlah admin! Beli bot ini untuk mengakses penuh.")
            return
        
        os.system("python src/run.py")

        # Menanyakan pengguna apakah ingin menyimpan hasil
        while True:
            save_result = input(Fore.CYAN + "Apakah Anda ingin menyimpan hasil akun PAYCO ke Internal Storage? (y/n): ").lower()
            if save_result == 'y':
                # Pindahkan file result.txt ke /sdcard/
                try:
                    shutil.move('result.txt', '/sdcard/result.txt')
                    print(Fore.GREEN + "File berhasil dipindahkan ke /sdcard/result.txt")
                except FileNotFoundError:
                    print(Fore.RED + "Anda bukanlah admin! Beli bot ini untuk mengakses penuh.")
                except Exception as e:
                    print(Fore.RED + f"Gagal memindahkan file: {e}")
                break  # Keluar dari perulangan jika input valid
            elif save_result == 'n':
                # Menghapus file result.txt
                try:
                    os.remove('result.txt')
                    print(Fore.YELLOW + "File result.txt berhasil dihapus. Akun tidak disimpan.")
                except FileNotFoundError:
                    print(Fore.RED + "Anda bukanlah admin! Beli bot ini untuk mengakses penuh.")
                except Exception as e:
                    print(Fore.RED + f"Kesalahan saat menghapus file: {e}")
                break  # Keluar dari perulangan jika input valid
            else:
                print(Fore.RED + "Kesalahan: Masukkan 'y' untuk ya atau 'n' untuk tidak.")  # Pesan kesalahan jika input tidak valid

    elif choice == '2':
        if not os.path.exists("reset.py"):
            print(Fore.RED + "Anda bukanlah admin! Beli bot ini untuk mengakses penuh.")
            return
        os.system("python reset.py")
    elif choice == '3':
        # Membuka URL menggunakan subprocess
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
        
        # Validasi input, hanya menerima angka 0-4
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
