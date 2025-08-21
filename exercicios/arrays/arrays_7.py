import time
inicio = time.perf_counter()

tamanho_Lista = 1000
novoArr = []

for i in range(1, tamanho_Lista + 1):
    novoArr.append(i)

escolha = int(input("Escolha um número: "))

i = 0
while i < len(novoArr) and novoArr[i] != escolha:
    i += 1

fim = time.perf_counter()

if i < len(novoArr):
    print(f"O número {escolha} está na posição {i}. O script demorou {(fim - inicio):.3f} segundos")
else:
    print(f"Não foi possivél identificar o número, certifique-se que o número seja até {tamanho_Lista}. O script demorou {(fim - inicio):.3f} segundos")
