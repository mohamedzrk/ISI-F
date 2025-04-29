const express = require('express');
const app = express();

// Simula búsqueda de vuelos
app.get('/flights', (req, res) => {
  const { ori, dst, date } = req.query;
  // Retorno estático o generado aleatoriamente
  res.json([
    { proveedor: 'ProveedorA', ori, dst, date, price: 120 },
    { proveedor: 'ProveedorB', ori, dst, date, price: 150 }
  ]);
});

app.listen(4000, () => {
  console.log('search-flight listening on 4000');
});
