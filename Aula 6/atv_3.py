resistencia = 6
entrada = input()

def mover(resistencia, entrada, total_itens):
    entrada = entrada.split(' ')
    movimento_atual = entrada[0]
    if resistencia <= 0:
        print('A correnteza está muito forte... não consigo continuar.')
        return -1
    elif movimento_atual.lower() == "linguado":
        resistencia += 1
        print('Obrigada, Linguado! Vamos rápido!')
    elif movimento_atual.lower() == "polvo":
        resistencia -= 3
        print('Cuidado com os servos da bruxa!')
    elif movimento_atual == '~':
        movimento_atual = ''
        resistencia -= 1
    else:
        total_itens += int(movimento_atual)
        resistencia -= 1
    entrada = entrada[1:]
    # print(movimento_atual)
    # print(entrada)
    if (resistencia <= 0):
        return -1
    elif len(entrada) == 0:
        return total_itens
    else:
        entrada = ' '.join(entrada)
        return mover(resistencia, entrada, total_itens)
    
total_itens = mover(resistencia, entrada, total_itens=0)
if total_itens > 0:
    print(f'Eric foi salvo! E Ariel ainda guardou {total_itens} bugigangas na sua gruta.')
else:
    print('A correnteza está muito forte... não consigo continuar.')
    print('O príncipe afundou... Úrsula venceu desta vez.')
    
