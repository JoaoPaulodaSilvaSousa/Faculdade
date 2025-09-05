let buscaBinaria = [];
let escolha = 400;
let encontrado = false;

for (let i = 0; i <= 1000; i++) {
    buscaBinaria[i] = i + 1;
}

let menor = 0;
let maior = buscaBinaria.length - 1;

while (menor <= maior) {
    let meio = Math.floor((menor + maior) / 2);

    if (buscaBinaria[meio] === escolha) {
        console.log("Achei no índice:", meio);
        encontrado = true;
        break;
    } else if (buscaBinaria[meio] < escolha) {
        menor = meio + 1;
    } else {
        maior = meio - 1;
    }
}

if (!encontrado) {
    console.log("Não encontrado");
}
