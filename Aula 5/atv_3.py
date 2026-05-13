vida = 100

def reacao_madeline(frase_madeline):
    if frase_madeline == 'Calma Badeline, nós vamos conseguir.':
        return vida + 25
    elif frase_madeline == 'Eu sei que somos capazes! Vamos em frente!':
        numero_de_respiracoes = int(input())
        return vida + (10 * numero_de_respiracoes)
    elif frase_madeline == 'Madeline, nós estamos com você. Continue!':
        return vida + 60
    else:
        return vida
      
def ataque_badeline(frase_badeline):
    if frase_badeline == 'Você não tem o que é necessário para escalar.':
        print('Eu nunca vou conseguir chegar ao topo :(')
        return vida - 20
    elif frase_badeline == 'NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!':
        print('NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!')
        return vida - 50
    else:
        return vida
    
while True:
    ataque = input()
    vida = ataque_badeline(ataque)
    if vida <= 0:
        print('Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima.')
        break
    if vida >= 150:
        print('Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista.')
        break
    reacao = input()
    vida = reacao_madeline(reacao)
    if vida <= 0:
        print('Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima.')
        break
    if vida >= 150:
        print('Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista.')
        break
    
    
    
    