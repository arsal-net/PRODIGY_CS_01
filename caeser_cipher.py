def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift value for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters are unchanged

    return result

def main():
    while True:
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter shift value (0-25): "))

        if shift < 0 or shift > 25:
            print("Invalid shift value. Please enter a value between 0 and 25.")
            continue

        result = caesar_cipher(message, shift, mode)
        print(f"Result: {result}")

        another = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
