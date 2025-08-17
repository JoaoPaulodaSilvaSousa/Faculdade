function calc() {
    let num_entrevistados = document.querySelector("#num_entrevistados").value.trim();
    let so_IOS = document.querySelector("#IOS").value.trim();
    let so_Android = document.querySelector("#Android").value.trim()
    let idade_usu = document.querySelector("#idade").value.split(",").map(x => Number(x.trim())).filter(x => !isNaN(x));
    let res = document.querySelector("#res");

    function media_idade(arr) {
        let soma = arr.reduce((a, b) => a + b ,0);
        return arr.length > 0 ? soma / arr.length : 0;
    }
    let idade_media = media_idade(idade_usu);

    res.innerHTML = `O número de pessoas entrevistados hoje foram ${num_entrevistados}.<br>
    ${so_IOS} usuários escolheream IOS e ${so_Android} escolheram Android.<br>
    A idade média é ${idade_media.toFixed(1)}`
}

