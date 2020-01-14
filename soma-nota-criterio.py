import psycopg2
con = psycopg2.connect(dbname="transparencia", user="esc-tce", password="123456")
cur = con.cursor()

#Calcular media das notas por criterio
cur.execute('select id from empenho')

select_empenho = cur.fetchall()
for registro_empenho in select_empenho:
    for id_empenho in registro_empenho:
        print(id_empenho)
        cur.execute('select nota_empenho_por_criterio.nota from empenho, nota_empenho_por_criterio where nota_empenho_por_criterio.id_empenho = empenho.id and empenho.id = {};'.format(id_empenho))
        select_nota = cur.fetchall()
        soma = 0
        for registro_nota in select_nota:
            for nota in registro_nota:
                soma += nota
    cur.execute('update empenho set nota = {} where id = {}'.format(soma, id_empenho))
    con.commit()
    print(soma)       


