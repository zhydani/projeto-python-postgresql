import psycopg2
from datetime import date
from datetime import datetime
con = psycopg2.connect(dbname="transparencia", user="esc-tce", password="123456")
cur = con.cursor()

#ETAPAS PARA SOMENTE O >>>EMPENHO<<<
#PRIMEIRO -> Verificar existencia de relatorio
cur.execute('select id from empenho where existencia_relatorio is true')
select_existencia_relatorio = cur.fetchall()
for registro_empenho in select_existencia_relatorio:
    for id_empenho in registro_empenho:
        print('este eh o id', id_empenho)
        cur.execute('select id from matriz_tce')
        select_matriz = cur.fetchall()
        for registro_matriz in select_matriz:
            for id_matriz in registro_matriz:
                print('critério >>>', id_matriz)
                cur.execute('select criterio from matriz_tce where id = {}'.format(id_matriz))
                select_criterio = cur.fetchall()
                for registro_criterio in select_criterio:
                    for criterio in registro_criterio:
                        print(criterio)
                        cur.execute('select {} from empenho where id = {}'.format(criterio, id_empenho))
                        select_tipo = cur.fetchall()
                        for registro_tipo in select_tipo:
                            for tipo in registro_tipo:
                                print(tipo)
                                if tipo is not None:
                                    cur.execute('select nota_ponderada from matriz_tce where id = {}'.format(id_matriz))
                                    select_nota = cur.fetchall()
                                    for registro_nota in select_nota:
                                        for nota in registro_nota:
                                            print(nota)
                                            cur.execute('insert into nota_empenho_por_criterio (id_matriz_tce, id_empenho, nota, data) values ({}, {}, {}, now());'.format(id_matriz, id_empenho, nota))
                                            con.commit()
                                elif tipo is None:
                                    nota = int(0)
                                    cur.execute('insert into nota_empenho_por_criterio (id_matriz_tce, id_empenho, nota, data) values ({}, {}, {}, now());'.format(id_matriz, id_empenho, nota))
                                    con.commit()

cur.execute('select id from empenho where existencia_relatorio is false')
select_rel_false = cur.fetchall()
for registro_false in select_rel_false:
    for id_empenho_false in registro_false:
        print('este eh o id', id_empenho_false)
        cur.execute('select id from matriz_tce')
        select_matriz_false = cur.fetchall()
        for registro_matriz_false in select_matriz_false:
            for id_matriz_false in registro_matriz_false:
                print('critério >>>', id_matriz_false)
                cur.execute('select criterio from matriz_tce where id = {}'.format(id_matriz_false))
                select_criterio_false = cur.fetchall()
                for registro_criterio_false in select_criterio_false:
                    for criterio_false in registro_criterio_false:
                        print(criterio_false)
                        cur.execute('select {} from empenho where id = {}'.format(criterio_false, id_empenho_false))
                        select_tipo_false = cur.fetchall()
                        for registro_tipo_false in select_tipo_false:
                            for tipo_false in registro_tipo_false:
                                print(tipo_false)
                                nota_false = int(0)
                                cur.execute('insert into nota_empenho_por_criterio (id_matriz_tce, id_empenho, nota, data) values ({}, {}, {}, now());'.format(id_matriz_false, id_empenho_false, nota_false))
                                con.commit()
con.close()

#Calcular media das notas por criterio
