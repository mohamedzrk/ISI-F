const express = require('express');
const cors = require('cors');
const axios = require('axios');
const app = express();

app.use(cors());

const SEARCH_URL = process.env.SEARCH_SERVICE_URL || 'http://search-flight:4000';

app.get('/flights', async (req, res) => {
  try {
    const response = await axios.get(`${SEARCH_URL}/flights`, { params: req.query });
    res.json(response.data);
  } catch (e) {
    res.status(500).json({ error: 'gateway error' });
  }
});

app.listen(3001, () => {
  console.log('API Gateway listening on 3001');
});
