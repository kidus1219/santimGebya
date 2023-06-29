import React from 'react';
import ReactDOM from 'react-dom/client';
import "./index.css"
import Profile from "./pages/Profile";
const App = () => {
  return  <Profile />
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <App />
);