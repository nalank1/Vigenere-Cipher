###encryption
def encrypt(text, key):
    text = text.upper()
    key = key.upper()
    encrypted_text = []

    numbered_key = [ord(i) - ord('A') for i in key]
    numbered_text = [ord(i) - ord('A') for i in text]

    for i in range(len(numbered_text)):
        numbered_text[i] = chr(((numbered_text[i] + numbered_key[i % len(numbered_key)]) % 26) + ord('A'))
        encrypted_text.append(numbered_text[i])
    return ''. join(encrypted_text)
        

###decryption
def decrypt(text, key):
    text = text.upper()
    key = key.upper()
    decrypted_text = []

    numbered_key = [ord(i) - ord('A') for i in key]
    numbered_text = [ord(i) - ord('A') for i in text]

    for i in range(len(numbered_text)):
        numbered_text[i] = chr(((numbered_text[i] - numbered_key[i % len(numbered_key)]) % 26) + ord('A'))
        decrypted_text.append(numbered_text[i])
    return ''. join(decrypted_text)

###main
def main():
    text = input("Enter the text: ")
    key = input("Enter the key: ")
    encrypted_text = encrypt(text, key)
    print(f"Encrypted text: {encrypted_text}")
    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")