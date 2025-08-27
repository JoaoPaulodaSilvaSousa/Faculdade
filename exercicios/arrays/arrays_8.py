buscaBinaria = []

for i in range(1, 1001):
    buscaBinaria.append(i)

escolha = int(input("Escolha um número: "))
menor = 0
maior = len(buscaBinaria) - 1
encontrado = False

while menor <= maior:
    meio = (maior + menor) // 2

    if buscaBinaria[meio] == escolha:
        print("Achei!")
        encontrado = True
        break
    elif buscaBinaria[meio] < escolha:
        menor = meio + 1
    else:
        maior = meio - 1

if not encontrado:
    print("Não encontrado.")
