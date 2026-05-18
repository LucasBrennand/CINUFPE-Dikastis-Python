alunos = {}

def adicionar_atividade(atividade):
    atividades_aluno_split = atividade.split(' ')
    nome_aluno = atividades_aluno_split[0]
    atividade_aluno = atividades_aluno_split[1]
    nota_atividade = atividades_aluno_split[2]
    
    if nome_aluno in alunos:
        alunos[nome_aluno][atividade_aluno] = nota_atividade
    else:
        alunos[nome_aluno] = {atividade_aluno: nota_atividade}

qtd_informacoes = int(input(""))
for i in range(qtd_informacoes):
    atividades_aluno = input()
    adicionar_atividade(atividades_aluno)
    
qtd_acoes = int(input(""))    
for i in range(qtd_acoes):
    comando = input()
    
    if comando == "adicionar":
        atividades_aluno = input("")
        adicionar_atividade(atividades_aluno)
        
    elif comando == "buscar":
        nome_busca = input("")
        if nome_busca in alunos:
            print(f"{nome_busca}:")
            for chave, valor in alunos[nome_busca].items():
                print(f'-{chave}: {valor}')
            print()
        else:
            print(f"{nome_busca} nao existe no sistema")
            print()
            
    elif comando == "consultar":
        atividade_busca = input("")
        alunos_com_atividade = []
        alunos_sem_atividade = []
        
        for aluno, info in alunos.items():
            if atividade_busca in info:
                nota = info[atividade_busca]
                alunos_com_atividade.append((aluno, nota))
            else:
                alunos_sem_atividade.append(aluno)
        
        if len(alunos_com_atividade) == 0:
            print(f"Ninguem possui a avaliacao {atividade_busca}")
            print()
        else:
            print(f"{atividade_busca}:")
            for nome, nota in alunos_com_atividade:
                print(f"-{nome}: {nota}")
                
            if len(alunos_sem_atividade) == 0:
                print("Nao possuem: ")
            else:   
                print(f"Nao possuem: {', '.join(alunos_sem_atividade)}")
            print()