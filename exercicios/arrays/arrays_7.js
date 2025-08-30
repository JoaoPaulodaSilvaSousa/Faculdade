let novoArr = []
let escolha = 1111
let lista = 1000

for (let i = 0; i <=1000; i++) {
    novoArr[i] = i+1
}
    
let i = 0
 while (i<novoArr.length && novoArr[i] != escolha) {
    i++;
 }

 if (i < novoArr.length) {
    console.log(`A sua escolha foi ${escolha} e está na posição ${i}`)
 } else {
    console.log(`O seu número passou do máximo de ${lista}`)
 }