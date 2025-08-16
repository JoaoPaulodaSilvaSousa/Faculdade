const inicio = Date.now();

let lista_num = [];
for (let i = 0; i < 1000000; i++) {
    lista_num[i] = i + 1;
}
const fim = Date.now();
const segundos = (fim-inicio) / 1000;

console.log(lista_num);
console.log(`${segundos} segundos`);