import psycopg2
con = psycopg2.connect(dbname="transparencia", user="esc-tce", password="123456")
cur = con.cursor()

#Calcular media das notas por criterio
cur.execute('select id from municipio')

select_municipio = cur.fetchall()
for registro_municipio in select_municipio:
    for id_municipio in registro_municipio:
        print(id_municipio)
        #NOTA EMPENHO
        cur.execute('select nota from empenho where id_municipio = {}'.format(id_municipio))      
        select_nota_por_empenho = cur.fetchall()
        count_empenho = 0
        soma_empenho = 0
        for registro_nota_por_empenho in select_nota_por_empenho:
            for nota_por_empenho in registro_nota_por_empenho:
                print(nota_por_empenho)
                count_empenho+=1
                soma_empenho += nota_por_empenho
        #NOTA LIQUIDACAO
        #cur.execute('select nota from liquidacao where id_municipio = {}'.format(id_municipio))      
        #select_nota_por_liquidacao = cur.fetchall()
        #count_liquidacao = 0
        #soma_liquidacao = 0
        #for registro_nota_por_liquidacao in select_nota_por_liquidacao:
        #    for nota_por_liquidacao in registro_nota_por_liquidacao:
        #        print(nota_por_liquidacao)
        #        count_liquidacao +=1
        #        soma_liquidacao += nota_por_liquidacao
        #NOTA PAGAMENTO
        #cur.execute('select nota from pagamento where id_municipio = {}'.format(id_municipio))      
        #select_nota_por_pagamento = cur.fetchall()
        #count_pagamento = 0
        #soma_pagamento = 0
        #for registro_nota_por_pagamento in select_nota_por_pagamento:
        #    for nota_por_pagamento in registro_nota_por_pagamento:
        #        print(nota_por_pagamento)
        #        count_pagamento +=1
        #        soma_pagamento += nota_por_pagamento
    media_empenho = soma_empenho/count_empenho
    #media_liquidacao = soma_liquidacao/count_liquidacao
    #media_pagamento = soma_pagamento/count_pagamento
    cur.execute('insert into nota_total (data, id_municipio) values (now(), {})'.format(id_municipio))
    con.commit()
    cur.execute('select id from nota_total where id_municipio = {}'.format(id_municipio))
    select_nota_total = cur.fetchall()
    for registro_nota_total in select_nota_total:
        for id_nota_total in registro_nota_total:
            print(id_nota_total)
            cur.execute('update nota_total set media_empenho = {} where id = {}'.format(media_empenho, id_nota_total))
            con.commit()
            #cur.execute('update nota_total set media_liquidacao = {} where id = {}'.format(media_liquidacao, id_nota_total))
            #con.commit()
            #cur.execute('update nota_total set media_pagamento = {} where id = {}'.format(media_pagamento, id_nota_total))
            #con.commit()
    print(media_empenho)


