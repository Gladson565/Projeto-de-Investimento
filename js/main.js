fetch("http://127.0.0.1:8000/api/equacao-reta-grafico", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      x1: valor1,
      y1: valor2,
      x2: valor3,
      y2: valor4
    })
  })
  .then(res => res.json())
  .then(data => {
    const imagem = new Image();
    imagem.src = `data:image/png;base64,${data.grafico_base64}`;
    document.body.appendChild(imagem);
  })
  .catch(() => {
    document.getElementById("erro").innerText = "Erro de conexão com o servidor.";
  });
  