const readline = require('readline');

// Cria interface para ler entrada do usuário
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Pergunta ao usuário
rl.question("Digite um número entre 1 e 101: ", function(resposta) {
    let escolha = parseInt(resposta); // converte para número

    let novoArr = [];
    for (let i = 0; i <= 100; i++) {
        novoArr[i] = i + 1;
    }

    let menor = 0;
    let maior = novoArr.length - 1;
    let achei = false;

    while (menor <= maior) {
        let meio = Math.floor((menor + maior) / 2);

        if (novoArr[meio] === escolha) {
            console.log("Achei o número na posição:", meio);
            achei = true;
            break;
        } else if (novoArr[meio] < escolha) {
            menor = meio + 1;
        } else {
            maior = meio - 1;
        }
    }

    if (!achei) {
        console.log("Nada encontrado.");
    }

    rl.close(); // fecha o readline
});
