"""
Classe Contato
Atributos: nome(str), telefone(str), data_de_inclusao(date), email(str)
Classe construtora: nome, telefone, email
Metodo cadastrar_email: entrada de cep, acrescenta um dicionario ao final da lista endereco
"""

# imports #
import json
import requests
from datetime import date

class Contato:
  def __init__(self, id, nome, telefone, email):
    self.id = id
    self.nome = nome.title()
    self.telefone = telefone
    self.data_de_inclusao = date.today()
    self.email = email
    self.endereco = []

  def consulta(self, cep, complemento):
    try:
      cep = cep.replace('-', '')
      url = f'https://viacep.com.br/ws/{cep}/json/'
      headers = {'User-Agent': 'Autociencia/1.0'}
      resposta = requests.request('GET', url, headers=headers)
      conteudo = resposta.content.decode('utf-8')
      resposta.close()
      endereco = (json.loads(conteudo))
      endereco['complemento'] = complemento
      self.endereco.append(endereco)
    except:
      pass
