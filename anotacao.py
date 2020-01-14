#ex.: empenho 1, requisito 1 != de null? entao nota 5,32 e assim por diante
lista = ['dt_emissao', 'numero', 'valor', 'id_classificacao_orcamentaria', 'id_fornecedor_credor', 'servico_produto']
for i in range(len(lista)):
    cur.execute('select {} from empenho where numero is not null'.format(lista[i]))
    
recset = cur.fetchall()
print (recset)
for rec in recset:
    print(rec)
    cur.execute('select id from empenho where numero = %s', (rec))
    id_empenho = cur.fetchall()
    for i in id_empenho:
        cur.execute('select nota_ponderada from matriz_tce where id = 2')
        nota = cur.fetchall()
        for n in nota:
            cur.execute('insert into nota_empenho_por_criterio (id_matriz_tce, id_empenho, nota) values (%s,%s,%s);', (2, i, n))
#depois somar todos os requisitos do empenho 1
#inserir na tabela
con.commit()
con.close()
print('saiu')




        cur.execute('select {} from empenho where {} is not null'.format(i, i))
        requisito = cur.fetchall()
        print(requisito)












import psycopg2
from datetime import date
con = psycopg2.connect(dbname="transparencia", user="esc-tce", password="123456")
cur = con.cursor()

#PRIMEIRO -> Verificar existencia de relatorio
cur.execute('select id from empenho where existencia_relatorio is true')
select = cur.fetchall()
for registro in select:
    for i in registro:
        print('este eh o id', i)
        lista = ['dt_emissao', 'numero', 'valor', 'id_classificacao_orcamentaria', 'id_fornecedor_credor', 'servico_produto']
        for l in range(len(lista)):
            cur.execute('select {} from empenho where id = {}'.format(lista[l], i))
            verificacao = cur.fetchall()
            for ver in verificacao:
                for v in ver:
                    print(v)
                    cur.execute('select id from matriz_tce')
                    select_matriz = cur.fetchall()
                    for reg in select_matriz:
                        for r in reg:
                            print('critério >>>', r, 'da matriz')










cur.execute('select nota_ponderada from matriz_tce where id = {}'.format(id_matriz))
                select_nota = cur.fetchall()
                for registro_nota in select_nota:
                    for nota in registro_nota:
                        print(nota)