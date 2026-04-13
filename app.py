from flask import Flask, send_from_directory

app = Flask(__name__)  # HARUS DI ATAS

@app.route('/')
def home():
    return "<h1>Hello dari Python di PWA!</h1>"

@app.route('/manifest.json')
def manifest():
    return send_from_directory('.', 'manifest.json')

@app.route('/service-worker.js')
def sw():
    return send_from_directory('.', 'service-worker.js')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
