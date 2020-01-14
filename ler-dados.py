import psycopg2
from datetime import date

def connect():
    con = psycopg2.connect(dbname="dadosabertos", user="esc-tce", password="123456")
    con.close()
    

def insert():
    con = psycopg2.connect(dbname="dadosabertos", user="esc-tce", password="123456")
    cur = con.cursor()
    cur.execute('insert into ranking (id, cidade, nota, data) values (default,%s,%s,now());', (cidade, nota))
    con.commit()
    con.close()

def view():
    con = psycopg2.connect(dbname="dadosabertos", user="esc-tce", password="123456")
    cur = con.cursor()
    cur.execute('select servico_produto from empenho, municipio where empenho.id_municipio = municipio.id and municipio.id = 1')
    recset = cur.fetchall()
    print (recset)
    for rec in recset:
        print (rec)
    con.close()
    
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