def calcular_macas(dia):
  if dia == 0:
    return 0
  elif dia == 1:
    return 1
  else:
    return calcular_macas(dia - 1) + calcular_macas(dia - 2)
    
dia_colheita = int(input())    
quantidade_macas = calcular_macas(dia_colheita)

print('Espelho, espelho meu, quantas maçãs a árvore deu?')
print(f'A árvore rendeu {quantidade_macas} maçãs no dia {dia_colheita}.')

if quantidade_macas < 7:
  print('Oh não! A colheita não foi suficiente para os sete anões.')
else:
  resto = quantidade_macas % 7
  macas_por_anao = quantidade_macas // 7
  
  print(f'Cada anão receberá {macas_por_anao} maçã(s) e Branca de Neve ficará com a sobra de {resto} maçã(s).')
  if resto == 0:
    print('A divisão foi perfeita! Nenhuma maçã sobrou para a torta da Branca de Neve.')