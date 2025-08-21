novoArr = []

for i in range(1,1001):
    novoArr.append(i)
escolha = int(input("Digite um número"))
menor = 0
maior = len(novoArr) - 1
meio = (menor + maior)//2

while menor <= maior:
    chute = novoArr[meio]

    if chute == escolha:
    print("Achei")
    break
elif chute < escolha:
menor = meio
else:
maior = meio
