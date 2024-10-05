import React, { useState } from 'react';
import StarMap from './components/StarMap';

function App() {
  const [exoplanetRa, setExoplanetRa] = useState(50);  // Example RA
  const [exoplanetDec, setExoplanetDec] = useState(30); // Example Dec

  return (
    <div className="App">
      <h1>Exoplanet Starmap</h1>
      {/* You could add input controls for setting RA and Dec dynamically */}
      <StarMap exoplanetRa={exoplanetRa} exoplanetDec={exoplanetDec} />
    </div>
  );
}

export default App;
