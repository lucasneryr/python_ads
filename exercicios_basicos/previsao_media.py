

print(f"{"-" * 5} Previsão de Nota Mínima Necessária {"-" * 5}\n")

media_objetivo = int(input("Qual seria a média desejada?\nMédia desejada: "))
# Perguntar qual a média que o usuário precisa?

provas_total = int(input(f"{"-" * 15}\nQual é o total de provas que você fará?\nTotal de provas: "))
# Perguntar quantas provas são no total.

provas_feitas = int(input(f"{"-" * 15}\nQuantas provas você já fez?\nProvas feitas: "))
# Perguntar quantas provas ainda faltam para serem feitas.

notas = []

print(f"{"-" * 15}\nAdicione agora uma nota de cada vez!")

for i in range (provas_feitas):
    nota = int(input(f"\nNota {i+1}: "))
    notas.append(nota)
# Pedir ao usuário para informar uma nota de cada vez.
    # Coloca todas as notas dentro de uma lista.

media_necessaria = ((media_objetivo * provas_total) - sum(notas)) / (provas_total - provas_feitas)

# Calcular a média necessária.
    # Somar todas as notas e dividir pela quantidade total de notas.
    # Verificar quanto de nota é necessário para ir da média atual para a média necessária.
    # Dividir o valor necessário pela quantidade de provas que ainda faltam.

print(f"Você precisa tirar no mínimo {media_necessaria} em cada prova restante para alcançar a média {media_objetivo}")
# Informar o usuário quanto ele precisa tirar no mínimo em cada prova para atingir a média desejada.