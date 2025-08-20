const now = require("performance-now");

let inicio = now();


let lista_num = [];
for (let i = 0; i < 1000000; i++) {
    lista_num[i] = i + 1;
}

let fim = now();
console.log(`${lista_num}. Executado em ${((fim - inicio) / 1000).toFixed(3)} s`);