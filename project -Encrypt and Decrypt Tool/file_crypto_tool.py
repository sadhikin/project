from cryptography.fernet import Fernet
import os

# 1. Generate a new key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved as 'secret.key'.")

# 2. Load an existing key from file
def load_key():
    if not os.path.exists("secret.key"):
        print("[!] Key file not found. Generate a key first.")
        return None
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# 3. Encrypt a text file
def encrypt_file(input_path, output_path, key):
    try:
        with open(input_path, "rb") as file:
            data = file.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        with open(output_path, "wb") as enc_file:
            enc_file.write(encrypted)
        print(f"[+] File encrypted and saved as '{output_path}'.")
    except Exception as e:
        print("[!] Error encrypting file:", e)

# 4. Decrypt a file
def decrypt_file(input_path, output_path, key):
    try:
        with open(input_path, "rb") as file:
            encrypted_data = file.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_data)
        with open(output_path, "wb") as dec_file:
            dec_file.write(decrypted)
        print(f"[+] File decrypted and saved as '{output_path}'.")
    except Exception as e:
        print("[!] Error decrypting file:", e)

# 5. Menu system
def main():
    while True:
        print("\n====== File Encryption/Decryption Tool ======")
        print("1. Generate Secret Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            key = load_key()
            if key:
                inp = input("Enter the path of the text file to encrypt: ")
                out = input("Enter the name for the encrypted file: ")
                encrypt_file(inp, out, key)
        elif choice == "3":
            key = load_key()
            if key:
                inp = input("Enter the path of the encrypted file: ")
                out = input("Enter the name for the decrypted file: ")
                decrypt_file(inp, out, key)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice. Try again.")

if __name__ == "__main__":
    main()
