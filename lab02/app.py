from flask import Flask, render_template, request, json # type: ignore
from cipher.caesar import CaesarCipher


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/caesar")
def caesar():
    return render_template('caesar.html')


@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypt_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypt_text}"  # sửa lại tên biến từ `encrypted_text` thành `encrypt_text`


@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypt_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypt_text}"  # sửa lại tên biến từ `decrypted_text` thành `decrypt_text`


# main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)