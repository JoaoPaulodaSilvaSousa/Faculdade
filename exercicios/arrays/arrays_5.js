let lista_num = []

for (let i = 0; i<1000; i++) {
    lista_num[i] = i +1;
}
const menor = lista_num[0];
const maior = lista_num[999];

console.log(lista_num)
console.log(`Esse é o menor número da lista: ${menor}`)
console.log(`Esse é o maior número da lista: ${maior}`)