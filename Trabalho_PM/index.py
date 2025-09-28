with open(r'c:\Users\João Paulo\Documents\GitHub\Faculdade\Trabalho_PM\estoque.txt', 'r', encoding='utf-8') as arquivo:
    estoque = [linha.strip() for linha in arquivo.readlines()]

nomes = [linha.split()[0] for linha in estoque]

def buscar_estoque(nomes):
    duplicados = set([nome for nome in nomes if nomes.count(nome) > 1])
    if duplicados:
        return f"Produtos duplicados encontrados: {', '.join(duplicados)}. Remova ou edite."
    else:
        return "Não há duplicidade em seu estoque. Tudo certo por aqui."

resultado = buscar_estoque(nomes)

for item in estoque:
    print(item)
    
print(resultado)