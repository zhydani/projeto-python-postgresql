from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
import psycopg2


app = Flask("__name_")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:1@localhost:5432/transparencia'
db = SQLAlchemy(app)

#TABELA EMPRESA
class Empenho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dt_emissao = db.Column(db.String(120), unique=False)
    dt_create = db.Column(db.String(120), unique=False)
    numero = db.Column(db.String(120), unique=False)
    valor = db.Column(db.String(120), unique=False)
    existencia_relatorio = db.Column(db.String(120), unique=False)
    id_municipio = db.Column(db.Integer, unique=False)
    servico_produto = db.Column(db.String(120), unique=False)
    id_classificacao_orcamentaria = db.Column(db.Integer, unique=False)
    id_fornecedor_credor = db.Column(db.Integer, unique=False)

    def __init__(self, dt_emissao, dt_create, numero, valor, existencia_relatorio, id_municipio, servico_produto, id_classificacao_orcamentaria, id_fornecedor_credor):
        self.dt_emissao = dt_emissao
        self.dt_create = dt_create
        self.numero = numero
        self.valor = valor
        self.existencia_relatorio = existencia_relatorio
        self.id_municipio = id_municipio
        self.servico_produto = servico_produto
        self.id_classificacao_orcamentaria = id_classificacao_orcamentaria
        self.id_fornecedor_credor = id_fornecedor_credor

  

@app.route('/empenho', methods=['POST'])
def insertEmpresasoftware():
    data = request.get_json()
    newDt_emissao = data['dt_emissao']
    newDt_create = data['dt_create']
    newNumero = data['numero']
    newValor = data['valor']
    newExistencia_relatorio = data['existencia_relatorio']
    newId_municipio = data['id_municipio']
    newServico_produto = data['servico_produto']
    newId_classificacao_orcamentaria = data['id_classificacao_orcamentaria']
    newId_fornecedor_credor = data['id_fornecedor_credor']
    empenho = Empenho(newDt_emissao, newDt_create, newNumero, newValor, newExistencia_relatorio, newId_municipio, newServico_produto, newId_classificacao_orcamentaria, newId_fornecedor_credor)
    db.session.add(empenho)
    db.session.commit()
    return newNumero

@app.route("/")
def pesquisa():
    a = insertEmpresasoftware()
    b = (db.session.query(Empenho.id).filter_by(numero=a).first()).fetchall()
    return b

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5050")