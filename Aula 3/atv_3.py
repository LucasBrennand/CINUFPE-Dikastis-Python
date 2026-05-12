material = ""
qtd_uniformes = 0
qtd_isotonicos = 0
qtd_raquetes = 0
qtd_toalhas = 0
teve_sabotagem = False

# # while material.upper() != "FIM":
#     material = input()
#     match material.lower():
#         case "uniforme":
#             qtd_uniformes += 1
#             print(f"Tava faltando camisa! Agora temos {qtd_uniformes} uniforme(s)")
#         case "isotonico":
#             qtd_isotonicos += 1
#             print(f"Bora garantir a hidratação! Agora temos {qtd_isotonicos} isotônico(s)")
#         case "raquete":
#             qtd_raquetes += 1
#             print(f"Mais uma raquete saindo! Agora temos {qtd_raquetes} raquete(s)")
#         case "toalha":
#             qtd_toalhas += 1
#             print(f"Mais uma toalha saindo! Agora temos {qtd_toalhas} toalha(s)")
#         case "sabotagem":
#             teve_sabotagem = True
#             material_sabotado = input()
#             match material_sabotado.lower():
#                 case "uniforme":
#                     if qtd_uniformes > 0:
#                         qtd_uniformes -= 1
#                         print(f"O sueco está roubando as camisas de Hugo!")
#                 case "isotonico":
#                     if qtd_isotonicos > 0:
#                         qtd_isotonicos -= 1
#                         print(f"O sueco está sabotando a hidratação de Hugo!")
#                 case "raquete":
#                     if qtd_raquetes > 0:
#                         qtd_raquetes -= 1
#                         print(f"O sueco está roubando as raquetes de Hugo!")
#                 case "toalha":
#                     if qtd_toalhas > 0:
#                         qtd_toalhas -= 1
#                         print(f"O sueco está roubando as toalhas de Hugo!")
#         case _:
            # print("Opção inválida!")
            
while material.upper() != "FIM":
    material = input()
    
    if material.lower() == "uniforme":
        qtd_uniformes += 1
        print(f"Tava faltando camisa! Agora temos {qtd_uniformes} uniforme(s)")
    if material.lower() == "isotonico":
        qtd_isotonicos += 1
        print(f"Bora garantir a hidratação! Agora temos {qtd_isotonicos} isotônico(s)")
    if material.lower() == "raquete":
        qtd_raquetes += 1
        print(f"Mais uma raquete saindo! Agora temos {qtd_raquetes} raquete(s)")
    if material.lower() == "toalha":
        qtd_toalhas += 1
        print(f"Mais uma toalha saindo! Agora temos {qtd_toalhas} toalha(s)")
    if material.lower() == "sabotagem":
        teve_sabotagem = True
        material_sabotado = input()
        if material_sabotado == "uniforme":
            if qtd_uniformes > 0:
                qtd_uniformes -= 1
                print(f"O sueco está roubando as camisas de Hugo!")
        if material_sabotado == "isotonico":
            if qtd_isotonicos > 0:
                qtd_isotonicos -= 1
                print(f"O sueco está sabotando a hidratação de Hugo!")
        if material_sabotado == "raquete":
            if qtd_raquetes > 0:
                qtd_raquetes -= 1
                print(f"O sueco está roubando as raquetes de Hugo!")
        if material_sabotado == "toalha":
            if qtd_toalhas > 0:
                qtd_toalhas -= 1
                print(f"O sueco está roubando as toalhas de Hugo!")

            

print("Bora ver o relatório final dos materiais!")
print(f"Uniforme: {qtd_uniformes} unidade(s).")
print(f"Isotônico: {qtd_isotonicos}.")
print(f"Raquete: {qtd_raquetes} unidade(s).")
print(f"Toalha: {qtd_toalhas} unidade(s).")

if (qtd_uniformes == 0 and qtd_isotonicos == 0 and qtd_raquetes == 0 and qtd_toalhas == 0) and teve_sabotagem:
    print("Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!")
elif (qtd_uniformes == 0 and qtd_isotonicos == 0 and qtd_raquetes == 0 and qtd_toalhas == 0) and teve_sabotagem == False:
    print("Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta.")
elif qtd_uniformes == 0 or qtd_isotonicos == 0 or qtd_raquetes == 0 or qtd_toalhas == 0:
    print("Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!")
else:
    print("Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!")
    


                
            
    