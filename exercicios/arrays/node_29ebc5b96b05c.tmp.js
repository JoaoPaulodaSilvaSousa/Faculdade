let buscaBinaria = []
let escolha = 300

for (let i = 0; i <= 1000; i++) {
    buscaBinaria[i] = i + 1
}

let menor = 0;
let maior = 1000;
let encontrado

while (menor <= maior) {
    let meio = Math.floor((menor + maior) / 2)

    if (buscaBinaria[meio] === escolha) {
        encontrado = true
        console.log(buscaBinaria[meio])
        break
    } else if (buscaBinaria[meio] < escolha) {
        menor = meio + 1
    } else {
        maior = meio - 1
    }
}