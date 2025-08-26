let list = [];

function buscaBinaria(minhaEscolha) {
    for (let i = 0; i <= 1000; i++) {
        list[i] = i + 1
    }

    let menor = 0;
    let maior = list.length - 1;
    
    while (menor <= maior) {
        const meio = parseInt((menor + maior) / 2);

        let valor = list[meio]

        if (valor === minhaEscolha) {
            return meio;
        } if (valor > minhaEscolha) {
            maior = meio - 1
        } else {
            menor = meio + 1
        }
    }
}

console.log(buscaBinaria(500));