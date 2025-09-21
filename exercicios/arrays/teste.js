const botao = document.getElementById("btnMostrar");

  botao.addEventListener("click", function() {
    // Pega o valor digitado
    let valor = document.getElementById("meuInput").value;

    // Mostra no alert
    alert(`Olá, ${valor}!`);
  });