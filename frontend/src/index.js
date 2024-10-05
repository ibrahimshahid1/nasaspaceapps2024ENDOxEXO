// Correct index.js file

import React from 'react';       // Only import React once
import ReactDOM from 'react-dom'; // ReactDOM is needed to render the app
import './index.css';            // Include any stylesheets (if applicable)
import App from './App';         // Your main App component
import reportWebVitals from './reportWebVitals';  // Optional for performance monitoring

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')  // React will render the app in the 'root' div in your HTML
);

// Optional performance reporting (you can remove this if you don't need it)
reportWebVitals();
