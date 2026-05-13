resistencia = 6
total_itens = 0
entrada = input()

def mover(resistencia, entrada, total_itens):
    resistencia -= 1
    entrada = entrada.split(' ')
    movimento_atual = entrada[0]
    if resistencia <= 0:
        print('A correnteza está muito forte... não consigo continuar.')
        return -1
    elif movimento_atual.lower() == "linguado":
        resistencia += 2
        print('Obrigada, Linguado! Vamos rápido!')
    elif movimento_atual.lower() == "polvo":
        resistencia -= 2
        print('Cuidado com os servos da bruxa!')
    elif movimento_atual == '~':
        movimento_atual = ''
    elif int(movimento_atual) >= 0:
        total_itens += int(movimento_atual)
    else:
        movimento_atual = ''
    entrada = entrada[1:]
    # print(movimento_atual)
    # print(entrada)
    if (resistencia == 0):
        print('A correnteza está muito forte... não consigo continuar.')
        print('O príncipe afundou... Úrsula venceu desta vez.')
        return -1
    elif len(entrada) == 0:
        print(f'Eric foi salvo! E Ariel ainda guardou {total_itens} bugigangas na sua gruta.')
        return -1
    else:
        entrada = ' '.join(entrada)
        mover(resistencia, entrada, total_itens)
    
mover(resistencia, entrada, total_itens=0)