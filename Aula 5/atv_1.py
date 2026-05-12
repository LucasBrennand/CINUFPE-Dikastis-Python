def calcular_custo(energia_total, preco):
    return energia_total * preco

def calcular_energia(horas, potencia, ineficiencia):
    energia_inicial = potencia * horas
    acrescimo = energia_inicial * (ineficiencia/100)
    energia_total = energia_inicial + acrescimo
    if energia_total == 0:
        print("Parece que essa coisa nem ao menos funciona")
    elif energia_total > 0 and energia_total <= 100:
        print(f"Temos aqui uma máquina formidável, seu consumo de energia é {energia_total:.2f}")
    elif energia_total > 100 and energia_total <= 300:
        print(f"Você tem certeza que essa coisa não vai explodir? seu consumo de energia é {energia_total:.2f}")
    else:
        print("Você se importaria de jogar seus explosivos em qualquer outro lugar?")
    return energia_total
   
gasto_total = 0       
maquina_mais_cara = 0
n = int(input("qtd maquinas: ")) # QTD_maquinas
for x in range(n): 
    h = int(input("horas: ")) # Horas
    p = float(input("potencia: ")) # Potencia
    i = int(input("ineficiencia: ")) # Ineficiencia
    print(f"ineficiencia em porcentagem: {i}")
    g = float(input("preço: ")) # Preço
    energia_atual = 0
    energia_atual = calcular_energia(h, p, i)
    gasto_atual = calcular_custo(energia_atual, g)
    gasto_total += gasto_atual
    if gasto_atual > maquina_mais_cara:
        maquina_mais_cara = gasto_atual
print(f'Os gastos totais com as maquinas foi de {gasto_total:.2f}')
print(f'A máquina mais cara gasta um total de {maquina_mais_cara:.2f} para os cofres de Piltover')
    