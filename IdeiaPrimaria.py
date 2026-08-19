#Primeira ideia sera colocar em pratica os ensinamentos em phyotn que aprendi com minhas aulas 

risco = 0
palavras_chave = ["senha", "urgente", "pix", "clique","agora","link", "transferência", "código","prêmio","Ganhou","Premiado", "Retirar","receba","Resgatar","risco"]

# Criamos a lista vazia onde vamos guardar o que for encontrado (possiveis indicadores de risco 1.0)
indicadores_encontrados = []
#.lower serve para palavras chave começadas em minusculo ou maisculo
mensagem = input("Digite sua mensagem: ").lower()

for palavra in palavras_chave:
    if palavra.lower() in mensagem:
        risco += 1
        # Adiciona a palavra encontrada dentro da lista
        indicadores_encontrados.append(palavra)

print("\nQuantidade de sinais de risco:", risco)

#exibe as palavras capturadas 1.0
if len(indicadores_encontrados) > 0:
    print("\nIndicadores encontrados:")
    for indicador in indicadores_encontrados:
        print(f"- {indicador}")

print()

#classificao "Semafaro" de risco encontrado 1.0
if risco == 0:
    print("🟢💀 Status: Mensagem aparentemente segura.")
elif risco == 1:
    print("🟡💀 Status: Atenção moderada! Verifique quem enviou.")
    print("\nRecomendação:")
    print("Tenha cautela. Confirme a identidade do remetente por outro meio antes de responder.")
else:
    print("🔴💀 Status: CUIDADO EXTREMO: Mensagem duvidosa!, em caso de duvida entrar em contato com algum familiar de sua confiança")
    print("\nRecomendação:")
    print("Não clique em links, não forneça senhas nem códigos e não faça transferências.")
if len(indicadores_encontrados) > 0:
    print("\nIndicadores encontrados:")
    for indicador in indicadores_encontrados:
        print(f"- {indicador}")
else:
    print("\nNenhum indicador de risco encontrado.")
   
    