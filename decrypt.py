import os
import json
from encryption_module import decrypt_text
import hashlib

# read all folder content
path = input("Set your location to check\n")

# Get a list of all files in the folder
all_files = os.listdir(path)

# Filter only the TXT files
calcs_files = [file for file in all_files if file.endswith('.calcs')]

# Iterate through the TXT files and read them
for calcs_file in calcs_files:
    file_path = os.path.join(path, calcs_file)
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Content of {calcs_file}:\n{content}")

        # read the JSON format:
        data = json.loads(content)
        encryption_value = data.get("filecontents", "")
        print(encryption_value)

        # decrypt content
        encrypted_text = encryption_value
        decryption_key = "abcddcba12345698abcddcba12345698"  # IN UTF8
        decryption_iv = "abcddcba12345698abcddcba12345698"  # IN HEX
        decrypted_text = decrypt_text(encryption_value, decryption_key, decryption_iv)
        print("Decrypted text:", decrypted_text)
        # hash the text to compare the text
        hash_decrypted_text = hashlib.sha256(decrypted_text.encode()).hexdigest()
        hash_value = data.get("filehash", "")
        if hash_decrypted_text == hash_value:
            print("Hash is match!")
        else:
            print("Wrong Hash")
