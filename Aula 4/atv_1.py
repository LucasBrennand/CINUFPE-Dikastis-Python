frases = ['Que tiro foi esse?', 'Segura a marimba', 'Tá com raiva? Morde as costas', 'Bateu de frente é só rajadão']
frases_exclusivas = []

qtd_frases_novas = int(input(""))
for frase in range(qtd_frases_novas):
    nova_frase = input("")
    frases.append(nova_frase)

for frase in frases:
    if frase not in frases_exclusivas:
        frases_exclusivas.append(frase)

for frase in frases_exclusivas:
    print(f'"{frase}": {frases.count(frase)}')
    
frases.sort()
print(frases)