import React from 'react';
import ReactDOM from 'react-dom/client';
import Login from "./pages/Login"
import "./index.css"
const App = () => {
  return  <Login />
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <App />
);

//<React.StrictMode> // this makes it run twice aghhh