function buscaBinaria(array, escolha) {

    let inicio = 0;
    let fim = array.length - 1;

    while (inicio <= fim) {
        let meio = Math.floor((inicio + fim) / 2)

        if (array[meio] === escolha) {
            return meio;
        } else if (array[meio] < escolha) {
            inicio = meio +1
        } else {
            fim = meio - 1
        }
    }
    return -1;
}

//exercicio1 

let numeros = [];
for (let i = 0; i <1000; i++) {
    numeros[i] = i+1;
}

console.log(buscaBinaria(numeros,300))