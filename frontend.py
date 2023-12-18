from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    # Retrieve form data
    fichier_entree = request.form['fichier_entree']
    fichier_sortie = request.form['fichier_sortie']
    operation = 'dechiffrement'  # Assuming decryption for this example
    cle_chiffrement = request.form['cle_chiffrement']
    mode_chiffrement = request.form['mode_chiffrement']
    vecteur = request.form['vecteur']
    colonnes = request.form['colonnes']
    separateur = request.form['separateur']

    # Call the FastAPI endpoint for decryption
    url = 'http://localhost:8000/encrypt_file'
    payload = {
        "fichier_entree": fichier_entree,
        "fichier_sortie": fichier_sortie,
        "operation": operation,
        "cle_chiffrement": cle_chiffrement,
        "mode_chiffrement": mode_chiffrement,
        "vecteur": vecteur,
        "colonnes": colonnes,
        "separateur": separateur
    }
    
    response = requests.post(url, json=payload)

    try:
        result_message = json.loads(response.text).get('message', 'An error occurred.')
    except json.decoder.JSONDecodeError:
        result_message = 'An error occurred. Response was not valid JSON.'

    return render_template('index.html', result_message=result_message)

if __name__ == '__main__':
    app.run(debug=True)
