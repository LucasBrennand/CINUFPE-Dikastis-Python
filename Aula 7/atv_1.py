qtd_sugestoes = int(input())
temas = {}
temas_ordenados = []
maior_voto = -1
votos_nao_na_lista: True


for n in range(qtd_sugestoes):
  tema_input = input()
  tema_split = tema_input.split(' ')
  nome = tema_split[0]
  votos = tema_split[1]
  votos = int(votos)
  temas[nome] = votos

temas_ordenados = sorted(temas.items(), key=lambda item: item[1], reverse=True)

for tema, votos in temas_ordenados:
  print(f"{tema} {votos}")
