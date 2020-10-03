# imports #
from flask import Flask, render_template, request, redirect, url_for
from contato import Contato
import MySQLdb
conn = MySQLdb.connect(user='root', passwd='admin', host='127.0.0.1', port=3306)

app = Flask(__name__)

# Main #

contatos = []

@app.route('/')
def index():
    return render_template('lista.html', titulo='Agenda', agenda=contatos)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Contato')

@app.route('/contato', methods=['POST',])
def contato():
    acesso = request.form['acessar']
    return render_template('contato.html', tiulo='Contato', acesso=acesso, contatos=contatos)

@app.route('/endereco', methods=['POST',])
def endereco():
    nome = request.form['nome']
    cep = request.form['cep']
    complemento = request.form['complemento']
    for item in contatos:
        if item.nome == nome:
            item.consulta(cep, complemento)
    return redirect(url_for('index'))


@app.route('/criar', methods=['POST',])
def criar():
    id = len(contatos)
    nome = request.form['nome'].title()
    telefone = request.form['telefone']
    email = request.form['email']
    contato = Contato(id, nome, telefone, email)
    contatos.append(contato)
    return redirect(url_for('index'))


app.run(debug=True)
