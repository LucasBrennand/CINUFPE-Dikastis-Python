n = int(input())
tripulantes = ["Zaphod Beeblebrox", "Ford Prefect", "Arthur Dent", "Marvin"]
print("Édipo: Inicializando sistema de embarque. Tripulantes atuais: Zaphod Beeblebrox, Ford Prefect, Arthur Dent, Marvin")
for evento in range(n):
    nome_evento = input()
    acao = nome_evento.split(' ', 1)[0].strip()
    tripulante_lista = nome_evento.split(' ')[1:]
    if nome_evento[-1].isnumeric():
        indice = tripulante_lista[-1]
        tripulante_lista.pop()
    tripulante = " ".join(tripulante_lista)
        
    if acao.lower() == "mover":
        tripulantes.remove(tripulante)
        tripulantes.insert(int(indice), tripulante)
    elif acao.lower() == "embarcar":
        if tripulante == "Trillian":
            print("Finalmente alguém sensata a bordo! Bem-vinda, Trillian!")
        tripulantes.append(tripulante)
    elif acao.lower() == "priorizar":
        if tripulante == "Zaphod Beeblebrox":
            print("EU SOU O PRESIDENTE DA GALAXIA! Primeiro lugar é pouco!")
            tripulantes.remove("Zaphod Beeblebrox")
            tripulantes.insert(0, "Zaphod Beeblebrox")
        elif tripulante == "Ford Prefect":
            print("Sou um escritor do Guia! Mereço destaque!")
            tripulantes.remove("Ford Prefect")
            tripulantes.insert(0, "Ford Prefect")
        else:
            tripulantes.remove(tripulante)
            tripulantes.insert(0, tripulante)
    elif acao.lower() == "remover":
        if tripulante == "Marvin":
            tripulantes.remove("Marvin")
            print("Ninguem se importa comigo mesmo. Tchau")
        elif tripulante == "Arthur Dent":
            tripulantes.remove("Arthur Dent")
            print("Eu só queria poder tomar chá... vou descer no próximo planeta")
        elif tripulante in tripulantes:
            tripulantes.remove(tripulante)
        else:
            print("Tripulante não encontrado")
    
        
if len(tripulantes) == 0:
    print("Édipo: Graças à improbabilidade, os novos comandantes são: ninguém... a nave está vazia!")
else: 
    if len(tripulantes) >= 3:
        print(f'Édipo: Graças à improbabilidade, os novos comandantes são: {tripulantes[0]}, {tripulantes[1]} e {tripulantes[2]}.')
    elif len(tripulantes) == 2:
        print(f'Édipo: Graças à improbabilidade, os novos comandantes são: {tripulantes[0]} e {tripulantes[1]}.')
    elif len(tripulantes) == 1:
        print(f'Édipo: Graças à improbabilidade, os novos comandantes são: {tripulantes[0]}.')
        
    if len(tripulantes) > 3:
        print(f"Convocando tripulantes:")
        for nome in tripulantes[3:]:
            print(f"- {nome}")
