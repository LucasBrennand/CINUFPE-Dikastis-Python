itens_carol = input()
itens_carol_lista = itens_carol.split(", ")
print("Pedido recebido! Vamos alocar os itens nos caminhões disponíveis.")
itens_encontrados = []
itens_ja_recebidos = []
algum_item_encontrado = False

while True:
    itens_caminhao = input()
    if itens_caminhao == "--" or len(itens_carol_lista) == 0:
        break
    itens_caminhao_lista = itens_caminhao.split(", ")
    print(f"Itens do caminhão: {itens_caminhao_lista}")
    for item in itens_caminhao_lista:
        if item in itens_carol_lista:
            algum_item_encontrado = True
            itens_encontrados.append(item)
            itens_ja_recebidos.append(item)
            itens_carol_lista.remove(item)
            print(f"Itens encontrados: {itens_encontrados}")
        elif item in itens_ja_recebidos:
            itens_ja_recebidos.append(item)
            itens_encontrados.append(item)
            algum_item_encontrado = True
    if algum_item_encontrado:
        print(f"Ótimo, esse caminhão trouxe {itens_encontrados}!")
        algum_item_encontrado = False
        itens_encontrados = []
    else:
        print("Não encontramos nada que a Carol pediu nesse caminhão.")
        
    if len(itens_carol_lista) != 0:
        print(f"Ainda precisamos de {itens_carol_lista}.")
    else:
        break
            
if len(itens_carol_lista) == 0:
    print("Conseguimos! A Carol ficará muito feliz :)")
else:
    print("Não conseguimos reunir todos os itens que a Carol precisa :(")
    
    