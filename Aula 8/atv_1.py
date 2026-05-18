try:
    livre_nome = input()
    qtd_dias_atraso = int(input())
    if qtd_dias_atraso < 0:
        raise ValueError("negativo")
    
    valor_multa = qtd_dias_atraso * 2.5
    
    print(f"Livro: {livre_nome}")
    print(f"Dias de atraso: {qtd_dias_atraso}")
    print(f"Valor da multa: R$ {valor_multa:.2f}")
    
except ValueError as e:
    if str(e) == "negativo":
        print("Erro: os dias de atraso não podem ser negativos.")
    else:
        print("Erro: você deve digitar um número inteiro para os dias de atraso.")
