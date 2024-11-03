import subprocess
import os

# URL yang ingin dibuka
url = "https://t.me/forumkt"

# Perintah untuk membuka URL di browser sesuai sistem operasi
if os.name == 'nt':  # Untuk Windows
    subprocess.run(["start", url], shell=True)
elif os.name == 'posix':  # Untuk Linux atau Mac
    subprocess.run(["xdg-open", url])
else:
    print("Sistem operasi tidak didukung.")
