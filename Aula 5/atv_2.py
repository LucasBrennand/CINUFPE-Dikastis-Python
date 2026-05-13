total_recursos = int(input())
populacao_piltover = int(input())
populacao_zaun = int(input())
situacao_zaun = input()


def calcular_taxa(populacao_zaun, populacao_piltover, situacao_zaun):
    if situacao_zaun == "desastre":
        taxa_zaun = 0.9
    elif situacao_zaun == "crise":
        taxa_zaun = 0.8
    elif situacao_zaun == "critica":
        taxa_zaun = 0.7
    elif situacao_zaun == "normal":
        taxa_zaun = 0.6
    elif situacao_zaun == "tranquilo":
        taxa_zaun = 0.5
    else:
        populacao_total = populacao_zaun + populacao_piltover
        taxa_zaun = populacao_zaun / populacao_total
    return taxa_zaun

def distribuir_recursos(taxa_zaun, total_recursos):
    taxa_piltover = 1 - taxa_zaun
    recursos_zaun = total_recursos * taxa_zaun
    recursos_piltover = total_recursos * taxa_piltover
    return [recursos_zaun, recursos_piltover]

def mensagem(recursos_zaun, recursos_piltover):
    razao = recursos_zaun/recursos_piltover
    if razao >= 0.9:
        print("Zaun receberá uma bolada!!!")
    elif razao >=0.8 and razao < 0.9:
        print("Quase que Piltover ficava sem nada, pobrezinhos...")
    elif razao >= 0.7 and razao < 0.8:
        print("O negócio vai ficar bom para Zaun hein.")
    elif razao >= 0.6 and razao < 0.7:
        print("Parece que Zaun ainda precisa de ajuda.")
    elif razao >= 0.5 and razao < 0.6:
        print("As coisas estão meio apertadas para Zaun.")
    else:
        print("A situação não está muito favorável para Zaun...")
         
taxa_zaun = calcular_taxa(populacao_zaun, populacao_piltover, situacao_zaun)
recursos_zaun = distribuir_recursos(taxa_zaun, total_recursos)[0]
recursos_piltover = distribuir_recursos(taxa_zaun, total_recursos)[1]
print(f'Foi decidido que será {recursos_piltover:.1f} para Piltover e {recursos_zaun:.1f} para Zaun!')
mensagem(recursos_zaun, recursos_piltover)
        