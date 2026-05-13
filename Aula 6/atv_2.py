n = int(input())
qtd_movimentos = 0

def movimentos(n):
    if n == 1:
        return 1
    qtd_movimentos = movimentos(n - 1) + 1 + movimentos(n - 1)
    return qtd_movimentos
   
qtd_movimentos = movimentos(n)  
print(f'Bela moveu os {n} livros em {qtd_movimentos} movimentos para o Pedestal de Marfim.')