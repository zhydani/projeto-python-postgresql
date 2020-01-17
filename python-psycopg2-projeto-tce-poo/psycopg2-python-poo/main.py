import psycopg2
from pprint import pprint
import json


x =  '{ "name":"John", "age":2, "nome": "nome"}'
y = json.loads(x)
#con = psycopg2.connect(dbname="transparencia", user="esc-tce", password="123456")
#cur = con.cursor()

#conectar no nosso querido banco com o psycopg2
class DatabaseConnection:
    
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='transparencia' user='esc-tce' host='localhost' password='123456' port='5432'" 
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Não foi possível conectar ao banco de dados")

    def create_table_pessoa(self):
        create_table_pessoa_command = "CREATE TABLE pessoa(id serial PRIMARY KEY, nome varchar(100))"
        self.cursor.execute(create_table_pessoa_command)
    
    def create_table_empresa_software(self):
        create_table_es_command = "CREATE TABLE public.empresa_software(CONSTRAINT empresa_software_pkey PRIMARY KEY (id))INHERITS (public.pessoa)"
        self.cursor.execute(create_table_es_command)

    def create_table_municipio(self):
        create_table_municipio_command = "CREATE TABLE public.empresa_software(url_dados character varying(100), id_empresa_software integer, CONSTRAINT municipio_pkey PRIMARY KEY (id), CONSTRAINT id_empresa_software FOREIGN KEY (id_empresa_software) REFERENCES public.empresa_software (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION NOT VALID)INHERITS (public.pessoa)"
        self.cursor.execute(create_table_municipio_command)

    def insert_fornecedor_credor(self):
        ##registro = REGISTRO TAL
        insert_fornecedor_credor_command = "INSERT INTO fornecedor_credor(id, nome, validar_cpf_cnpj, cpf_cnpj) VALUES ({}, {}, {});".format() #TAL REGISTRO NO FORMATO
        pprint(insert_fornecedor_credor_command)
        self.cursor.execute(insert_fornecedor_credor_command)

    def insert_new_record(self, nome, idade):
        insert_new_record = "INSERT INTO pet(name, age) VALUES ({}, {})".format(nome, idade) 
        self.cursor.execute(insert_new_record)
    
    def query_all(self):
        self.cursor.execute("SELECT * FROM pet")
        cats = self.cursor.fetchall()
        for cat in cats:
            pprint("each pet: {}".format(cat))


if __name__== '__main__':
    database_connection = DatabaseConnection()
    #database_connection.create_table()
    database_connection.insert_new_record(str(y["nome"]), y["age"])
    #database_connection.query_all()