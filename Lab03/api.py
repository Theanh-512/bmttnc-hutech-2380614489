from flask import Flask, request, jsonify
from cipher.rsa import RSACipher
from cipher.ecc import ECCcipher

app = Flask(__name__)
rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.json
    message = data.get('message')
    key_type = data.get('key_type')
    private_key, public_key = rsa_cipher.load_keys()

    if not message or not key_type:
        return jsonify({'error': 'Missing message or key_type'}), 400

    key = public_key if key_type == 'public' else private_key if key_type == 'private' else None
    if not key:
        return jsonify({'error': 'Invalid key type'}), 400

    encrypted_b64 = rsa_cipher.encrypt(message, key)
    return jsonify({'encrypted_message': encrypted_b64})

@app.route('/api/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    data = request.json
    ciphertext_b64 = data.get('ciphertext')
    key_type = data.get('key_type')
    private_key, public_key = rsa_cipher.load_keys()

    if not ciphertext_b64 or not key_type:
        return jsonify({'error': 'Missing ciphertext or key_type'}), 400

    key = public_key if key_type == 'public' else private_key if key_type == 'private' else None
    if not key:
        return jsonify({'error': 'Invalid key type'}), 400

    try:
        decrypted_message = rsa_cipher.decrypt(ciphertext_b64, key)
        return jsonify({'decrypted_message': decrypted_message})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/rsa/sign', methods=['POST'])
def rsa_sign_message():
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({'error': 'Missing message'}), 400
    private_key, _ = rsa_cipher.load_keys()
    signature_b64 = rsa_cipher.sign(message, private_key)
    return jsonify({'signature': signature_b64})

@app.route('/api/rsa/verify', methods=['POST'])
def rsa_verify_signature():
    data = request.json
    message = data.get('message')
    signature_b64 = data.get('signature')
    if not message or not signature_b64:
        return jsonify({'error': 'Missing message or signature'}), 400

    _, public_key = rsa_cipher.load_keys()
    is_verified = rsa_cipher.verify(message, signature_b64, public_key)
    return jsonify({'is_verified': is_verified})

ecc_cipher = ECCcipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)