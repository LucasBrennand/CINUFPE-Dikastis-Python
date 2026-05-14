entrada = ""
pessoas = []

while entrada.lower() != "fim":
    naturalidade = ""
    profissao = ""
    idade = 0
    grupo = ""
    valor = ""
    pessoa_existe = False
    
    entrada = input()
    entrada_splitada = entrada.split(' ')
    nome = entrada_splitada[0]
    if entrada_splitada[1] == "profissao":
        profissao = entrada_splitada[1]
    elif entrada_splitada[1] == "naturalidade":
        naturalidade = entrada_splitada[1]
    elif entrada_splitada[1] == "grupo":
        grupo = entrada_splitada[1]
    valor = entrada_splitada[2]
    
    pessoa = {
        "nome": nome,
        "naturalidade": naturalidade,
        "profissao": profissao,
        "grupo": grupo,
        "idade": idade
    }
    
    for pessoa_busca in pessoas: # busca todas pessoas
        for nome_busca in pessoa.values(): # busca apenas o nome
            if nome_busca == nome: # se nome digitado ja existe
                print(f"nome buscado: {nome_busca}")
                print(f"nome digitado: {nome}")
                print(nome_busca == nome)
                # print("pessoa existe")
                pessoa_existe = True
            if pessoa_existe:
                if pessoa_busca['naturalidade'] == "":
                    pessoa_busca['naturalidade'] = naturalidade
                if pessoa_busca['profissao'] == "":
                    pessoa_busca['profissao'] = profissao
                if pessoa_busca['grupo'] == "":
                    pessoa_busca['grupo'] = grupo
                if pessoa_busca['idade'] == 0:
                    pessoa_busca['idade'] = idade
    if pessoa_existe == False:
        print("Essa pessoa não existe")
        pessoas.append(pessoa)
        
    for i in pessoas:
        print(i)
            
                
    