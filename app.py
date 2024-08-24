from flask import Flask, request, render_template

app = Flask(__name__)


###encryption
def encrypt(text, key):
    text = text.upper()
    key = key.upper()
    encrypted_text = ''

    numbered_key = [ord(i) - ord('A') for i in key]
    numbered_text = [ord(i) - ord('A') for i in text]

    for i in range(len(numbered_text)):
        numbered_text[i] = chr(((numbered_text[i] + numbered_key[i % len(numbered_key)]) % 26) + ord('A'))
        encrypted_text += numbered_text[i]
    return encrypted_text
        

###decryption
def decrypt(text, key):
    text = text.upper()
    key = key.upper()
    decrypted_text = ''

    numbered_key = [ord(i) - ord('A') for i in key]
    numbered_text = [ord(i) - ord('A') for i in text]

    for i in range(len(numbered_text)):
        numbered_text[i] = chr(((numbered_text[i] - numbered_key[i % len(numbered_key)]) % 26) + ord('A'))
        decrypted_text += numbered_text[i]
    return decrypted_text

###main
def main():
    text = input("Enter the text: ")
    key = input("Enter the key: ")
    encrypted_text = encrypt(text, key)
    print(f"Encrypted text: {encrypted_text}")
    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    text = request.form['text']
    key = request.form['key']
    encrypted_text = encrypt(text, key)
    decrypted_text = decrypt(encrypted_text, key)
    return render_template('index.html', encrypted_text=encrypted_text, decrypted_text=decrypted_text)
    



if __name__ == '__main__':
    app.run(debug=True)