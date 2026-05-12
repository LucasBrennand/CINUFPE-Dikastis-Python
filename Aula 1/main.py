import math
# ATIVIDADE 1
def atv_1():
    P = int(input("Digite a quantidade de packs de ferro: "))
    if (3 <= P):
        V = int(P / 3)
        F = P % 3
        print(V)
        print(F)
    else:
        print("Nao é possivel dividir os packs igualmente")
        
# ATIVIDADE 2 FALTA
def atv_2():
# Hogsmeade (X: 34, Y: 110, Z: 220)
# Kakariko (X: 0, Y: 64, Z: 0)
# Solitude (X: 140, Y: 200, Z: 456)
# D² = (X1 - X2)² + (Z1 - Z2)²
    x = int(input("Digite sua coordenada X: "))
    z = int(input("Digite sua coordenada Z: "))
    
    H = ((x - 34)**2) + ((z - 220)**2)
    H = math.sqrt(H)
    K = ((x - 0)**2) + ((z - 0)**2)
    K = math.sqrt(K)
    S = ((x - 140)**2) + ((z - 456)**2)
    S = math.sqrt(S)
    print(f"Distancia para Hogsmeade: {H:.2f}")
    print(f"Distancia para Kakariko: {K:.2f}")
    print(f"Distancia para Solitude: {S:.2f}")
        
    
# ATIVIDADE 3
def atv_3():
    L = int(input("Informe a largura: "))
    A = int(input("Informe a altura: "))
    if(1 <= L and 2 <= A):
        B = L**2 * A
        print(B)
    else:
        print("Dimensão inválida")

# ATIVIDADE 4 FALTA
def atv_4():
    A = int(input("Informe a media de A: "))
    L = int(input("Informe a media de L: "))
    P = int(input("Informe a media de P: "))
    H = int(input("Informe a quantidade de horas: "))
  
    x = (A + L + abs(A - L)) / 2
    m = (x + P + abs(x - P)) / 2
    m = int(m * H)
    print(m)
    
atv_4()
    
# ATIVIDADE 5
def atv_5():
    D = int(input("Digite quantos dias: "))
    C = int(input("Digite a quantidade de casas: "))
    
    tickets_3_horas_reais = 20 * 10800 #Tickets em 3 horas reais = 216.000 tickets
    tickets_diurnio_3_horas_reais = tickets_3_horas_reais / 2 #Tickets no ciclo diurnio em 3 horas reais = 108.000
    tickets_possiveis_em_3_horas_por_dia = tickets_diurnio_3_horas_reais * D #Tickets em 3 horas no ciclo diurnio * qtd_dias
    T = int(tickets_possiveis_em_3_horas_por_dia / C) #Tickets possiveis / Casas
    print(T)
    
    
# ATIVIDADE 6
def atv_6():
    N = input("Digite o primeiro nome: ").lstrip()
    S = input("Digite o ultimo nome: ").lstrip()
    if N.isalpha() and S.isalpha() or N == "_" or S == "_":
        k = N + S
        k.lstrip()
        if (len(k) >= 3 and len(k) <= 16):
            print(k)
        else:
            print("Quantidade inválida de caracteres")
    else:
        print("Contém caractere inválida")

# ATIVIDADE 7
def atv_7():
    d = int(input("Digite quantos diamantes precisa: "))
    if d < 0:
        print("Valor inválido")
    elif d >= 1 and d <= 10:
        print("Arthur")
    elif d >= 11 and d <= 30:
        print("Luiz")
    elif d >= 31 and d <= 100:
        print("Pedro")
    else:
        print("Nenhum")

        
    

