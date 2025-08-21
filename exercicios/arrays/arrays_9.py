import time
inicio = time.perf_counter()

novoArr = []

for i in range(1, 1001):
    novoArr.append(i)

escolha = int(input("Digite um número: "))
menor = 0
maior = len(novoArr) - 1

while menor <= maior:
    meio = (menor + maior) // 2
    chute = novoArr[meio]

    print(f"Tentando índice {meio}, valor {chute}")

    if chute == escolha:
        fim = time.perf_counter()
        print(f"Achei! A sua escolha é o número {escolha}.")
        print(f"Executado em {(fim - inicio):.3f} segundos")
        break
    elif chute < escolha:
        menor = meio + 1
    else:
        maior = meio - 1
else:
    fim = time.perf_counter()
    print("Número não encontrado.")
    print(f"Executado em {(fim - inicio):.6f} segundos")
