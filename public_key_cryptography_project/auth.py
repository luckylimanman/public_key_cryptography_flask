from flask import Flask, render_template, request
# import sys
# import public_key_cryptography
# from public_key_cryptography import lcm, hcf, deco, enco
from public_key_cryptography import cryptography
# from public_key_cryptography.cryptography import pro
# from public_key_cryptography.cryptography import encryption
# from public_key_cryptography.cryptography import decryption
# sys.path.insert(0, 'public-key-cryptography/cryptography.py')


app = Flask(__name__)
app.config.from_object('config')


@app.route('/index/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    return render_template('index.html')


@app.route('/index/generate_key/', methods=['POST', 'GET'])
def generate_key():
    if request.method == 'POST':
        public_key_string, private_key_string = cryptography.generate_key(1)
        return render_template('auth/generate_key_result.html',
                               public_key=public_key_string,
                               private_key=private_key_string)
    return render_template('auth/generate_key.html')


@app.route('/index/encrypte_code/', methods=['POST', 'GET'])
def encrypte_code():
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        public_key = request.form['public_key']
        ciphertext = cryptography.encryption(plaintext, public_key)
        return render_template('/auth/encrypte_code_result.html',
                               ciphertext=ciphertext)
    return render_template('/auth/encrypte_code.html')


@app.route('/index/decrypte_code/', methods=['POST', 'GET'])
def decrypte_code():
    if request.method == 'POST':
        ciphertext = request.form['ciphertext']
        plaintext = cryptography.decryption(ciphertext)
        return render_template('/auth/decrypte_code_result.html',
                               plaintext=plaintext)
    return render_template('auth/decrypte_code.html')


@app.route('/prview/prview_result.html', methods=['POST', 'GET'])
def puview_result():
    return render_template('/pkc/prview_result.html')


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
