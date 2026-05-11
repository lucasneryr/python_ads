print(f"{"-" * 5} Previsão de Nota Mínima Necessária {"-" * 5}\n")

media_objetivo = int(input("Qual seria a média desejada?\nMédia desejada: "))
provas_total = int(input(f"{"-" * 15}\nQual é o total de provas que você fará?\nTotal de provas: "))
provas_feitas = int(input(f"{"-" * 15}\nQuantas provas você já fez?\nProvas feitas: "))

notas = []

# Pedir ao usuário para informar uma nota de cada vez.
print(f"{"-" * 15}\nAdicione agora uma nota de cada vez!")
for i in range (provas_feitas):
    nota = int(input(f"\nNota {i+1}: "))
    notas.append(nota)

# Calcular a média necessária.
media_necessaria = ((media_objetivo * provas_total) - sum(notas)) / (provas_total - provas_feitas)

# Informar o usuário quanto ele precisa tirar no mínimo em cada prova para atingir a média desejada.
print(f"Você precisa tirar no mínimo {media_necessaria} em cada prova restante para alcançar a média {media_objetivo}")
