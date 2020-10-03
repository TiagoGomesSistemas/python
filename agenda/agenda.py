# imports #
from flask import Flask, render_template, request, redirect, url_for
from contato import Contato

# Main #
app = Flask(__name__)

contatos = []

# index.html #
@app.route('/')
def index():
    return render_template('lista.html', titulo='Agenda', agenda=contatos)

# novo.html #
@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Contato')

# contato.html #
@app.route('/contato', methods=['POST',])
def contato():
    acesso = request.form['acessar']
    return render_template('contato.html', titulo='Contato', acesso=acesso, contatos=contatos)

# Adiciona novo endereço e retorna para index.html #
@app.route('/endereco', methods=['POST',])
def endereco():
    nome = request.form['nome']
    cep = request.form['cep']
    complemento = request.form['complemento']
    for item in contatos:
        if item.nome == nome:
            item.consulta(cep, complemento)
    return redirect(url_for('index'))

# Cria novo contato e retorna para index.html #
@app.route('/criar', methods=['POST',])
def criar():
    id = len(contatos)
    nome = request.form['nome'].title()
    telefone = request.form['telefone']
    email = request.form['email']
    contato = Contato(id, nome, telefone, email)
    contatos.append(contato)
    return redirect(url_for('index'))

# Chamada do app #
app.run(debug=True)
