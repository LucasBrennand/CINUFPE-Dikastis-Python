velocidade_IJ = int(input())
velocidade_LR = int(input())
dificuldade_inimigos = int(input())

pontuacao = (velocidade_IJ * velocidade_LR) / dificuldade_inimigos
if pontuacao <= 65000:
    print("BRUTAL! Ninguém jamais conseguiu alcançar as pontuações fantásticas do Jorel.")
elif pontuacao > 65000 and pontuacao <= 99000:
    print("INCRÍVEL! A dupla conseguiu alcançar o top 10 nas pontuações do jogo.")
elif pontuacao > 99000 and pontuacao <= 153000:
    print("SENSACIONAL!! Os jogadores conseguiram alcançar o pódio do jogo ao lado das outras pontuações do Jorel.")
else:
    print("IMPOSSÍVEL!!! A DUPLA IMPLACÁVEL FOI CAPAZ DE QUEBRAR O RECORDE INALCANÇÁVEL DO JOREL!")
