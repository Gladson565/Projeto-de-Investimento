exports.calcularInvestimento = (req, res) => {
    const { aporteMensal, taxaJuros, tempoMeses } = req.body;
  
    // Exemplo simples de juros compostos
    let montante = 0;
    for (let i = 1; i <= tempoMeses; i++) {
      montante = (montante + aporteMensal) * (1 + taxaJuros / 100);
    }
  
    res.json({ montante: montante.toFixed(2) });
  };
  