import time

inicio = time.perf_counter()

lista_num = []
for i in range(1, 1000001):
    lista_num.append(i)

fim = time.perf_counter()

print(f"{lista_num}. Executado em {(fim - inicio):.3f} s")
