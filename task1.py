# Caesar Cipher Implementation
# SkillCraft Technology Internship - Task 01

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # check if character is a letter
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(cipher_text, shift):
    return caesar_encrypt(cipher_text, -shift)

# Driver code
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted = caesar_encrypt(message, shift)
    print(f"Encrypted Message: {encrypted}")

    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Decrypted Message: {decrypted}")
