# ESTA DANDO RUNTIME ERROR

def classificar_alvo(nivel_ameaca, armado):
    if nivel_ameaca >= 7 and armado:
        return "Elite"
    elif nivel_ameaca >= 7 and armado == False:
        return "Executor"
    elif nivel_ameaca >= 4 and nivel_ameaca < 7 and armado:
        return "Veterano"
    elif nivel_ameaca >= 4 and nivel_ameaca < 7 and armado == False:
        return "Operador"
    elif nivel_ameaca < 4:
        return "Iniciante"
        
     
def analisar_tentativas(numeros_tentativas):
    tentativas_lista = []
    numeros_tentativas = numeros_tentativas.split(' ')
    for numero in numeros_tentativas:
        if numero != " ":
            tentativas_lista.append(int(numero))
    total_tentativas = len(tentativas_lista)
    if sum(tentativas_lista) % total_tentativas == 0:
        print(f"Missão Completa. | Manipulação temporal: {total_tentativas} tentativa(s)") 
        return True
    else:
        print(f'Missão Fracassou! ZERO não foi capaz de assassinar o alvo e acabou morrendo. Nunca descobrirá o que realmente aconteceu.')
        return False
    
def ataques_refletidos(numeros_ataques):
    favoritos = [3, 5]
    ataques_lista = []
    ataques_refletidos = 0
    numeros_ataques = numeros_ataques.split(' ')
    for numero in numeros_ataques:
        if numero != " ":
            numero = int(numero)
            ataques_lista.append(numero)
    for numero in ataques_lista:
        for numero_favorito in favoritos:
            if numero % numero_favorito == 0:
                ataques_refletidos += 1
                break
    print(f"Dragão refletiu {ataques_refletidos} ataque(s)!")

print("Entendo… Vamos começar do começo.")
dia_inicial = int(input())

missao_sucesso = False


while dia_inicial >= 0:
    print()
    print(f'====== Restam {dia_inicial} dias. ======')
    
    musica = input() # musica - autor
    musica_split = musica.split(' - ')
    nome_musica = musica_split[0]
    autor_musica = musica_split[1]
    
    print(f'Escutando: {nome_musica} - {autor_musica}')
    alvo = input() # nome - ameaca - armado
    nome_alvo = alvo.split(' - ')[0]    
    
    nivel_ameaca = int(alvo.split(' - ')[1])
    armado = alvo.split(' - ')[2]
    if armado.lower() == 'sim':
        armado = True
    elif armado.lower() == 'não' or armado.lower() == 'nao':
        armado = False
        
    if autor_musica == 'DJ Electrohead' and nome_alvo == 'DJ Electrohead':
        print("DJ Electrohead é morto na sua frente. Lhe avisaram para NÃO FALAR com ele.")
        dia_inicial -= 1
        continue
    
    classificacao = classificar_alvo(nivel_ameaca, armado)
       
    print(f"Analisando alvo: {nome_alvo}... Classificação: {classificacao}")
    
    tentativas = input()
    missao_sucesso = analisar_tentativas(tentativas)
    if missao_sucesso == False:
        break
    ataques_inimigos = input()
    ataques_refletidos(ataques_inimigos)
    dia_inicial -= 1
    
if missao_sucesso:
    print()
    print('====== FIM DAS MISSÕES ======')
    print('Parabéns Subject ZERO! Seu trabalho deve ser recompensado. Nova dose do seu remédio esta aqui.')
     