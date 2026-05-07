import math

print(f"{"-" * 5} Sistema de Notas {"-" * 5}\n")
qtd_notas = int(input("Quantas notas você gostaria de adicionar: "))
notas = []

for i in range (qtd_notas):
    nota = int(input(f"Nota {i+1}: "))
    if(nota < 0 or nota > 10):
        print("Nota inválida")
        break
    print("\n")
    notas.append(nota)
media = sum(notas) / len(notas)

print(f"Sua média foi: {media}")
if (media >= 7):
    print("Você foi aprovado!")
else:
    print("Você foi reprovado.")