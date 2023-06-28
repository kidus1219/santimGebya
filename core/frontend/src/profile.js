import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Profile from "./pages/Profile"
import PinPage from "./pages/PinPage";
import "./index.css"
document.addEventListener("DOMContentLoaded", () => {
  if ("basename" in DATA && window.location.pathname !== DATA.basename) {
    console.log("restarting");
    window.location.pathname = DATA.basename;
  }
}); // TODO more testing required
const App = () => {
  return (
    <BrowserRouter basename={DATA.basename}>
      <Routes>
          <Route path="/" element={<Profile />} />
          <Route path="/pin-page" element={<PinPage />} />
      </Routes>
    </BrowserRouter>
  );
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <App />
);

//<React.StrictMode> // this makes it run twice aghhh