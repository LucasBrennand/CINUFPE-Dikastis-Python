print("Bom dia, dona Maria! Aqui vão as músicas mais pedidas de hoje!")
musica = ""
qtd_musicas = 0
musica_setlist = "Setlist de músicas: "
while musica.lower() != "voa, voa brabuleta":
    musica = input("")
    if musica.lower() == "voa, voa brabuleta":
        break
    if qtd_musicas == 0:
        musica_setlist += musica
    else:
        musica_setlist += " - " + musica     
    qtd_musicas += 1
    
print(f"A quantidade de músicas selecionadas foi {qtd_musicas}")
print(musica_setlist)