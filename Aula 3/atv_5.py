dinheiro_inicial = int(input())
print(f"A família possui {dinheiro_inicial} ainda, talvez ele fique tranquilo hoje")

compra = ""
primeira_entrada = True
qtd_compras = 0
custo_total

while compra != "Amauri":
    compra = input()
    custo = int(input())
     
    if compra == "Amauri":
        if primeira_entrada:
            continue
        else:
            print("Sabia que vocês estão loucos, hora de encerrar essa loucura!")
            break
        
    if custo > 500000:
        print(f"Enlouqueceram de vez {custo} reais num(a) {compra}")
        break
    elif custo > dinheiro_inicial:
        print("Enlouqueceram? Vocês estão falidos")
        break
    else:
        print(f"Gastaram {custo} reais para comprar um(a) {compra}")
        
    if compra.lower() == "carro":
        modelo = input()
        if modelo.lower() == "chevette":
            print("chevette : Relembrando as origens será?")
        elif modelo.lower() == "jeep":
            print("jeep : Será que ele tá se preparando para outra aventura que não irá?")
        elif modelo.lower() == "bmw":
            print("bmw : Já to vendo o facebook dele cheio de foto me marcando 🙁")
        else:
            print("Não tem esse carro")