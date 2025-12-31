document.getElementById('temp').addEventListener('click', () => fetchData('/t'));
document.getElementById('weather').addEventListener('click', () => fetchData('/w'));

function fetchData(endpoint) {
  const output = document.getElementById('output');
  output.textContent = 'Lade Daten vom Server…';

  fetch(`http://127.0.0.1:5000${endpoint}`, { cache: 'no-cache' })  // Optional: verhindert Caching
    .then(response => {
      if (!response.ok) {
        throw new Error(`Server-Fehler: ${response.status} ${response.statusText}`);
      }
      return response.text();
    })
    .then(text => {
      output.textContent = text.trim();  // Entfernt überflüssige Leerzeichen/Zeilenumbrüche
    })
    .catch(err => {
      output.textContent = `Fehler: Server nicht erreichbar oder Abfrage fehlgeschlagen.\n\nDetails: ${err.message}\n\nStelle sicher, dass dein Python-Server läuft!`;
    });
}