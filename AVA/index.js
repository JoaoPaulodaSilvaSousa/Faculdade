function calc() {
    let num_entrevistados = document.querySelector("#num_entrevistados").value.trim();
    let so_IOS = document.querySelector("#IOS").value.trim();
    let so_Android = document.querySelector("#Android").value.trim();
    let idade_usu = document.querySelector("#idade").value
        .split(",")
        .map(x => Number(x.trim()))
        .filter(x => !isNaN(x));
    let res = document.querySelector("#res");

    function media_idade(arr) {
        let soma = arr.reduce((a, b) => a + b ,0);
        return arr.length > 0 ? soma / arr.length : 0;
    }
    let idade_media = media_idade(idade_usu);

    // Criar objeto com dados do dia
    let hoje = new Date().toLocaleDateString();
    let dadosDia = {
        data: hoje,
        entrevistados: Number(num_entrevistados),
        ios: Number(so_IOS),      // <-- Corrigido (era iso)
        android: Number(so_Android),
        mediaIdade: idade_media
    };

    // Recuperar histórico salvo
    let historico = JSON.parse(localStorage.getItem("pesquisa")) || [];

    // Adicionar dados do dia
    historico.push(dadosDia);

    // Salvar de volta no localStorage
    localStorage.setItem("pesquisa", JSON.stringify(historico));

    // Mostrar resultado do dia
    res.innerHTML = `📊 Pesquisa do dia ${hoje}<br>
        • ${dadosDia.entrevistados} entrevistados<br>
        • ${dadosDia.ios} usam iOS e ${dadosDia.android} usam Android<br>
        • Idade média: ${dadosDia.mediaIdade.toFixed(1)}`;
}

function mostrarHistorico() {
    let historico = JSON.parse(localStorage.getItem("pesquisa")) || [];
    let res = document.querySelector("#res");

    if (historico.length === 0) {
        res.innerHTML = "<p>⚠️ Nenhum dado salvo ainda</p>";
        return;
    }

    res.innerHTML = "<h2>📜 Histórico de pesquisas</h2>";
    historico.forEach(dia => {
        res.innerHTML += `<p>
        📅 ${dia.data}<br>
        👥 ${dia.entrevistados} entrevistados<br>
        📱 iOS: ${dia.ios}, 🤖 Android: ${dia.android}<br>
        🧑 Idade média: ${dia.mediaIdade.toFixed(1)}
        </p>`;
    });
}
