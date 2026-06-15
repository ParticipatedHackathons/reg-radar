import { useEffect, useState } from 'react';

function App() {
  const [status, setStatus] = useState('Loading...');

  useEffect(() => {
    fetch('http://localhost:8000/api/status')
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    return response.json();
  })
  .then((data) => setStatus(data.message))
  .catch((err) => {
    console.error(err);
    setStatus('Unable to reach backend');
  });
  });

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', margin: '2rem' }}>
      <h1>RegRadar</h1>
      <p>{status}</p>
      <section style={{ marginTop: '2rem' }}>
        <h2>RBI Circular Ingestion</h2>
        <p>Upload an RBI circular PDF and get a structured impact summary.</p>
        <p>This starter app includes the backend API and a simple dashboard placeholder.</p>
      </section>
    </div>
  );
}

export default App;
