const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

dotenv.config();
const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// Rotas
const investimentosRoute = require('./routes/investimentos');
app.use('/api/investimentos', investimentosRoute);

app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});
