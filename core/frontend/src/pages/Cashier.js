import React, { useState } from "react";
import CashierHeader from "../components/CashierHeader"
import { AiOutlineLogin } from "react-icons/ai";
import { RiLockPasswordFill } from "react-icons/ri";
import Header from "../components/Header";
import Footer from "../components/Footer";
import MainButton from "../components/MainButton";
import CashierBody from "../components/CashierBody";

const Cashier = () => {


  return (
      <div className="flex flex-col w-full h-screen text-center bg-gray-300">
          <CashierHeader merchant_id="ID001"/>
          <CashierBody/>
      </div>
  );
};
export default Cashier;
