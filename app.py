from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para buscar o CEP
@app.route('/buscar-cep/<cep>', methods=['GET'])
def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return jsonify(resposta.json())
    else:
        return jsonify({"erro": "CEP inválido ou não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
