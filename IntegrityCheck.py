import hashlib
import os
import time
import logging
logging.basicConfig(
    filename='ap.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

old_hashes = {}

def monitor_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                with open('ap.log', 'r', encoding="utf-8") as log:
                    stored_hash = log.read()
            except FileNotFoundError:
                stored_hash = " "

            old_hash = old_hashes.get(file_path, " ")

            current_hash = calculate_hash(file_path)
            if stored_hash != current_hash:
                with open('ap.log', 'a', encoding="utf-8") as log_update:
                    log_update.write(f"File Changed: {file_path}\n")
                    log_update.write(f"Old Hash: {old_hash}\n")
                    log_update.write(f"New Hash: {current_hash}\n\n")
                
                old_hashes[file_path] = current_hash

if __name__ == "__main__":
    monitored_directory = r'E:\ABC'

    while True:
        monitor_directory(monitored_directory)
        time.sleep(10)
