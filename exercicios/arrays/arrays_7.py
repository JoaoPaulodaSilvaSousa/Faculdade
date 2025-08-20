novoArr = []
for i in range(1, 1001): 
    novoArr.append(i)

escolha = int(input("Escolha um número: "))

i = 0
while novoArr[i] != escolha:  
    i += 1                     

print("Achei! Está na posição", i)
