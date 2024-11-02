import sys
import subprocess
import os

def run_script():
    while True:
        try:
            subprocess.run([sys.executable, "src/run.py"], check=True)
        except subprocess.CalledProcessError:
            print("An error occurred while running the script.")
            print("Attempting to install dependencies...")
            
            # Install dependencies
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
                print("Dependencies successfully installed.")
                continue
            except subprocess.CalledProcessError:
                print("Failed to install dependencies or run the script.")
                print("Please check your internet connection and try again.")
        except KeyboardInterrupt:
            break
        input("Press Enter to try again...")

if __name__ == "__main__":
    try:
        run_script()
    except:
        sys.exit()
