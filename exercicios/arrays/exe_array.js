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

let resultado = buscaBinaria(array,);

if (resultado === -1) {
    console.log(`Valor não encontrado: ${escolha}`);
} else {
    console.log(`Valor encontrado. Valor ${escolha}, na posição ${resultado}.`)
}


// Exercício 1: array de 1 a 1000
let array1 = []
for (let i = 0; i < 1000; i++) {
    array1[i] = i+1
}

console.log(buscaBinaria(array1, 300));