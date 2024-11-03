import shutil
import os
import subprocess

# Path file sumber dan tujuan
source = "result.txt"
destination = "/sdcard/result.txt"

try:
    # Memindahkan file
    shutil.move(source, destination)
    print("File berhasil dipindahkan.")
except FileNotFoundError:
    print("File tidak ditemukan.")
except PermissionError:
    print("Izin ditolak. Menjalankan 'termux-setup-storage' untuk memberikan akses.")
    try:
        # Menjalankan perintah untuk memberikan akses penyimpanan di Termux
        subprocess.run(["termux-setup-storage", "-y"], check=True)
        print("Silakan coba jalankan skrip ini lagi setelah memberikan izin.")
    except Exception as e:
        print(f"Terjadi kesalahan saat memberikan akses: {e}")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
