import psycopg2
from datetime import date

def connect():
    con = psycopg2.connect(dbname="dadosabertos", user="esc-tce", password="123456")
    con.close()
    
#primeiro somar todas as categorias com a tabela matriz tce -> nota tabela nota 
#especifica de empenho, liquidacao e pagamento onde o id for daquele empenho
def insert():
    con = psycopg2.connect(dbname="dadosabertos", user="esc-tce", password="123456")
    cur = con.cursor()
    #ex.: empenho 1, requisito 1 != de null? entao nota 5,32 e assim por diante
    cur.execute('select numero from empenho')
    recset = cur.fetchall()
    print (recset)
    for rec in recset:
        if(rec != null)
            print (rec)
    #depois somar todos os requisitos do empenho 1
    #inserir na tabela
    con.commit()
    con.close()

#segundo calcular a media de todos os empenhos, liquidacoes e pagamentos de certo municipio -> municipio id
def view():
    con = psycopg2.connect(dbname="dadosabertos", user="esc-tce", password="123456")
    cur = con.cursor()
    cur.execute('select servico_produto from empenho, municipio where empenho.id_municipio = municipio.id and municipio.id = 1')
    recset = cur.fetchall()
    print (recset)
    for rec in recset:
        print (rec)
    con.close()

#somar as notas depois com os requisitos de nota final que sao todos booleans e gerar a nota final na tabela final
def search(title="", author="", year="", isbn=""):
    con = psycopg2.connect(dbname="dadosabertos", user="esc-tce", password="123456")
    cur = con.cursor()
    cur.execute("select * from bool where title=? or author=? or isbn=?", (title, author, year, isbn))
    rows=cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = psycopg2.connect(dbname="dadosabertos", user="esc-tce", password="123456")
    cur = con.cursor()
    cur.execute('delete from book where id=?', (id))
    rows=cur.fetchall()
    con.close()
    return rows