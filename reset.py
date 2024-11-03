import os
import shutil
import subprocess

# Tentukan path untuk .env
env_path = os.path.join(os.getcwd(), '.env')

# Periksa apakah .env adalah file atau folder, lalu hapus
if os.path.isfile(env_path):
    os.remove(env_path)  # Hapus file .env
    print(".env file berhasil dihapus.")
elif os.path.isdir(env_path):
    shutil.rmtree(env_path)  # Hapus folder .env beserta isinya
    print("Folder .env berhasil dihapus.")
else:
    print(".env tidak ditemukan.")

# Jalankan perintah python src/run.py
try:
    result = subprocess.run(["python", "src/run.py"], check=True)
    print("Script src/run.py berhasil dijalankan.")
except subprocess.CalledProcessError as e:
    print(f"Error saat menjalankan script: {e}")
