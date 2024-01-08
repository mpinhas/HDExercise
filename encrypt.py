import os
import hashlib
import json
from encryption_module import encrypt_text

# read all folder content
path = input("Set your location to check\n")

# Get a list of all files in the folder
all_files = os.listdir(path)

# Filter only the TXT files
txt_files = [file for file in all_files if file.endswith('.txt')]

# Iterate through the TXT files and read them
for txt_file in txt_files:
    file_path = os.path.join(path, txt_file)
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Content of {txt_file}:\n{content}")
        # Hash the content
        hashed_string = content
        hashed_string = hashlib.sha256(hashed_string.encode()).hexdigest()
        print("SHA-256 hash:", hashed_string)
        # Encrypt the content

        #  Encrypt the content using AES with Key & IV with BASE64
        # Mode ECB, Input Raw, Output Raw
        encryption_key = "abcddcba12345698abcddcba12345698"  # IN UTF8
        encryption_iv = "abcddcba12345698abcddcba12345698"  # IN HEX
        text_to_encrypt = content
        encrypted_text = encrypt_text(text_to_encrypt, encryption_key, encryption_iv)
        print(encrypted_text)

        # Open a new calcs file for each file as JSON format
        file_data = {
            "filehash": hashed_string,
            "filecontents": encrypted_text
        }
        with open(os.path.join(path, f"{txt_file}.calcs"), "x") as file_encrypt:
            json_text = json.dumps(file_data, indent=2)
            file_encrypt.write(json_text)

print("all files.calcs was creating on the folder with all the information")
