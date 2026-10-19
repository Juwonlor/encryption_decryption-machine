
from cryptography.fernet import Fernet

# Load the secret key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)


def encrypt_file():
    filename = input("Enter the filename to encrypt: ")

    try:
        with open(filename, "rb") as file:
            original = file.read()
    except FileNotFoundError:
        print("Error: File not found. Check the filename and try again.")
        return

    encrypted = fernet.encrypt(original)

    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted)

    print("File encrypted successfully!")
    print("Encrypted file saved as:", filename + ".encrypted")


def decrypt_file():
    filename = input("Enter the encrypted filename: ")

    try:
        with open(filename, "rb") as file:
            encrypted = file.read()
    except FileNotFoundError:
        print("Error: Encrypted file not found. Check the filename and try again.")
        return

    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception:
        print("Error: Decryption failed. The key may be incorrect or the file may be damaged.")
        return

    if filename.endswith(".encrypted"):
        output_filename = filename[:-10] + ".decrypted"
    else:
        output_filename = filename + ".decrypted"

    with open(output_filename, "wb") as file:
        file.write(decrypted)

    print("File decrypted successfully!")
    print("Decrypted file saved as:", output_filename)


# Main menu
while True:
    print("\n=== File Encryption Tool ===")
    print("1. Encrypt file")
    print("2. Decrypt file")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        encrypt_file()
    elif choice == "2":
        decrypt_file()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
