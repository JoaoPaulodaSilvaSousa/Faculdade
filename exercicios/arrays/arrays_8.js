let buscaBinaria = []

for (let i = 0; i <= 1000; i++) {
    buscaBinaria[i] = i + 1
}
 menor = 0;
 maior = 1000;

 while (menor <= maior) {
    meio = Math.floor((menor + maior))/2

    if (buscaBinaria === meio)
        console.log(buscaBinaria[meio])
 }