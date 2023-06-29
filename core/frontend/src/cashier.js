import React from 'react';
import ReactDOM from 'react-dom/client';
import "./index.css"
import Cashier from "./pages/Cashier";
const App = () => {
  return  <Cashier />
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <App />
);