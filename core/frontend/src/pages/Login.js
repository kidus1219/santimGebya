import React, { useState } from "react";
import { AiOutlineLogin } from "react-icons/ai";
import { RiLockPasswordFill } from "react-icons/ri";
import Header from "../components/Header";
import Footer from "../components/Footer";
import MainButton from "../components/MainButton";

const Login = () => {
  const [pin, setPin] = useState('');
  const handleLogin = () => {
    if (isNaN(pin)) {
      alert("Login Failed: Only numbers allowed");
    } else if (pin.toString().length !== 4) {
      alert("Login Failed: Pin must be 4 digit");
    } else {
      DATA.mainButton.showProgress();
      fetch(DATA.loginApi, {
        method: "POST",
        headers: DATA.fetchHeaders,
        mode: "same-origin",
        body: JSON.stringify({ initData: DATA.initData, pin: pin }),
      })
        .then((resp) => resp.json())
        .then((data) => {
          DATA.mainButton.hideProgress();
          if (data.signal > 0) {
            alert(data.msg);
            DATA.goToTg(data.tgApi);
          } else {
            alert("Login Failed: " + data.msg);
          }
        })
        .catch((error) => {
          DATA.mainButton.hideProgress();
          alert("Something went wrong: " + error);
          // maybe alert also the status code
        });
    }
  };

  return (
    <>
      <Header
        pageTitle="Login"
        pageDesc="Enter your pin"
        pageIcon={<AiOutlineLogin size="40px" />}
      />
      <div className="root-core">
        <div className="flex leading-none gap-2 p-2">
          <RiLockPasswordFill />
          <label>PIN</label>
        </div>
        <input
          required
          type="password"
          onInput={(e) => setPin(e.target.value)}
        />
      </div>
      <Footer />
      <MainButton actors={[pin]} func={handleLogin} text="Login" />
    </>
  );
};
export default Login;
