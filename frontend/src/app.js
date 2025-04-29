import { useState } from 'react';
import axios from 'axios';

function App() {
  const [flights, setFlights] = useState([]);
  const [ori, setOri] = useState('');
  const [dst, setDst] = useState('');
  const [date, setDate] = useState('');

  const search = async () => {
    const res = await axios.get('http://localhost:3001/flights', {
      params: { ori, dst, date }
    });
    setFlights(res.data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Comparador de Vuelos</h1>
      <input placeholder="Origen" onChange={e=>setOri(e.target.value)} />
      <input placeholder="Destino" onChange={e=>setDst(e.target.value)} />
      <input type="date" onChange={e=>setDate(e.target.value)} />
      <button onClick={search}>Buscar</button>
      <ul>
        {flights.map((f,i)=>(
          <li key={i}>{f.proveedor} {f.ori}→{f.dst} {f.date} {f.price}€</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
