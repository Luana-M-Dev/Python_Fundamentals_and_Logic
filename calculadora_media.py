#%%

notas = []
soma_notas = 0

while True:
    nota = input("Digite a nota do aluno:")
    if nota == "":
        break
    notas.append(float(nota))
    soma_notas = soma_notas + float(nota)

if len(notas) == 0:
    print("Nenhuma nota inserida. Encerrando.")
    exit()

media = soma_notas / len(notas)


if media >= 7:
    print(f"O aluno está APROVADO! A média dele foi {media}")
elif media >=5:
    print(f"O aluno está de RECUPERAÇÃO! A média dele foi {media}")
else:
    print(f"O aluno está REPROVADO! A média dele foi {media}")
