import React from "react";
import { AiFillCopyrightCircle } from "react-icons/ai";
const Footer = () => {
  return (
    <div className="w-full flex justify-center gap-1 py-2 text-accent text-xs fixed bottom-0">
      <AiFillCopyrightCircle className="" />
      2023 All rights reserved!
    </div>
  );
};

export default Footer;
