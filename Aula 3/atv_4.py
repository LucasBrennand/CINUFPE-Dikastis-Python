doces = int(input())
jogador_1 = input()
jogador_2 = input()
vida_jogador_1 = 10
vida_jogador_2 = 10
x = 10 # doces nessa rodada
qtd_rodadas = int(doces / 10)
if doces % 10 != 0:
    x = doces % 10
    qtd_rodadas += 1
qtd_doces_jogador_1 = 0
qtd_doces_jogador_2 = 0
tem_arthur = True
numero_do_turno = 1
jogada_1 = ""
jogada_2 = ""
ganhador_rodada = ""
turno_empate = False

if (jogador_1 != "Arthur") and (jogador_2 != "Arthur"):
    tem_arthur = False
    print("Epa!!! E cadê o dono dos doces??")
else:
    print("A batalha vai começar!")
    if tem_arthur:
        for rodada in range(1, qtd_rodadas + 1):
            vida_jogador_1 = 10
            vida_jogador_2 = 10
            
            if (rodada == 1) and (doces % 10 != 0):
                print(f"Pra aquecer, essa primeira vale menos, só {x} doces!")
            else:
                x = 10
                print(f"Batalha número {rodada}!")
                
            while vida_jogador_1 > 0 or vida_jogador_2 > 0:
                jogada_1 = input()
                jogada_2 = input()
                if (jogada_1.lower() == "papel" and jogada_2.lower() == "papel") or (jogada_1.lower() == "pedra" and jogada_2.lower() == "pedra") or (jogada_1.lower() == "tesoura" and jogada_2.lower() == "tesoura"):
                    print("Eita, jogaram a mesma coisa dessa vez.")
                    turno_empate = True
                    numero_do_turno += 1
                elif jogada_1.lower() == "papel" and jogada_2.lower() == "pedra":
                    vida_jogador_1 += 2
                    vida_jogador_2 -= 2
                    numero_do_turno += 1
                elif jogada_1.lower() == "pedra" and jogada_2.lower() == "papel":
                    vida_jogador_1 -= 2
                    vida_jogador_2 += 2
                    numero_do_turno += 1
                elif jogada_1.lower() == "papel" and jogada_2.lower() == "tesoura":
                    vida_jogador_1 -= 3
                    vida_jogador_2 += 1
                    numero_do_turno += 1
                elif jogada_1.lower() == "tesoura" and jogada_2.lower() == "papel":
                    vida_jogador_1 += 1
                    vida_jogador_2 -= 3
                    numero_do_turno += 1
                elif jogada_1.lower() == "pedra" and jogada_2.lower() == "tesoura":
                    vida_jogador_2 -= 4
                    numero_do_turno += 1
                elif jogada_1.lower() == "tesoura" and jogada_2.lower() == "pedra":
                    vida_jogador_1 -= 4
                    numero_do_turno += 1
                else:
                    print("Opção inválida!")
                if vida_jogador_1 <= 0 or vida_jogador_2 <= 0:
                    if vida_jogador_1 > vida_jogador_2:
                        vida_jogador_2 = 0
                        ganhador_rodada = jogador_1
                        qtd_doces_jogador_1 += x
                        doces -= x
                    else:
                        vida_jogador_1 = 0
                        ganhador_rodada = jogador_2
                        qtd_doces_jogador_2 += x
                        doces -= x
                if turno_empate != True:
                    print(f"Esse turno terminou com {jogador_1} tendo {vida_jogador_1} de vida e {jogador_2} tendo {vida_jogador_2}!")
                turno_empate = False
                
                if vida_jogador_1 == 0 or vida_jogador_2 == 0:
                    break
            print(f"A rodada {rodada} vai para {ganhador_rodada}, que garante seus doces!")           