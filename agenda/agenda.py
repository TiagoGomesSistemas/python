# imports #
from flask import Flask, render_template, request, redirect, url_for
from contato import Contato
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:datascience@localhost:3306/agenda')

# Main #
app = Flask(__name__)

contatos = []
try:
    df = pd.read_sql_table('agenda', engine)
    for item in df[0]:
        contatos.append(item)
except:
    pass

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
            df = pd.DataFrame(contatos)
            df.to_sql(
                name='agenda',
                con=engine,
            )
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
    df = pd.DataFrame(contatos)
    df.to_sql(
        name='agenda',
        con=engine,
    )
    return redirect(url_for('index'))

# Chamada do app #
app.run(debug=True)
