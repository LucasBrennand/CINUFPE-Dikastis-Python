qtd_sugestoes = int(input())
temas = []
temas_ordenadas = []
maior_voto = -1
segundo_maior_voto = -1
menor_voto = -1

for n in range(qtd_sugestoes):
  tema_input = input()
  tema_split = tema_input.split(' ')
  nome = tema_split[0]
  votos = tema_split[1]
  tema = {
    "nome": nome,
    "votos": int(votos)
  }
  votos_atuais = tema['votos']
  if votos_atuais > maior_voto:
    maior_voto = votos_atuais
    temas.insert(0, tema)
  elif len(temas) >= 1:
    if votos_atuais < maior_voto and votos_atuais > temas[1]['votos']:
      temas.insert(1, tema)
    else:
      for tema in temas: # {'nome': 'BOB_ESPONJA', 'votos': 25}
        print(f'tema: {tema}')
        maior_votos_loop = -1
        for votos in tema.items():# ('nome', 'BOB_ESPONJA') ('votos', 25)
          print(votos[2])
          if votos[0] == 'votos':
            votos = int(votos[1])
            print(f'num: {votos}')
          if votos > maior_votos_loop:
            maior_votos_loop = votos
          else:
            temas.remove(tema)
            temas.append(tema)
          
          
      # if votos_atuais > temas[-1]['votos']:
      #   temas.insert(-1, tema)
      # else:
      #   temas.append(tema)
  
print("-"*20)
for tema in temas:
  print(f"{tema['nome']} {tema['votos']}")

print(temas)
  
  
#  5 10 4 0
#  5
#  10 5 4 0
#  6 12 25 5 8 9 8
#  6
#  12 6
#  25 12 6
#  25 12 6
#  25 12 6 8 
