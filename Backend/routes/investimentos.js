const express = require('express');
const router = express.Router();
const { calcularInvestimento } = require('../controllers/investimentosController');

router.post('/calcular', calcularInvestimento);

module.exports = router;
