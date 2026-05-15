participantes = {}
campos = []
entrada = ""

while True:
    participante_encontrado = False
    entrada = input()

    if entrada.lower() == "fim":
        break

    entrada_splitada = entrada.split()

    if len(entrada_splitada) != 3:
        continue
    nome = entrada_splitada[0]
    if nome not in participantes:
        participantes[nome] = {}
    campo = entrada_splitada[1]
    if campo not in campos:
        campos.append(campo)
    valor = entrada_splitada[2]
    participantes[nome][campo] = valor

for nome, informacoes in participantes.items():
    print(f"{nome}:")
    for campo, valor in informacoes.items():
        print(f"- {campo}: {valor}")
            
print("Faltam")

for nome, dados_participante in participantes.items():
    print(f"{nome}:")
    for campo in campos:
        if campo not in dados_participante:
            print(f"- {campo}")