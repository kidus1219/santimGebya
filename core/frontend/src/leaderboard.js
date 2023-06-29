import React from 'react';
import ReactDOM from 'react-dom/client';
import "./index.css"
import Leaderboard from "./pages/Leaderboard";
const App = () => {
  return  <Leaderboard />
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <App />
);