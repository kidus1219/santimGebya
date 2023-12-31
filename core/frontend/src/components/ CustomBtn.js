import React from "react";
import hagurashLogo from "../../public/images/hagurash_logo_a.jpg";
const CustomBtn = ({promptTxt, width, onclick,type}) => {
  return (
        <button type={type} className={`bg-button text-slate-100 rounded-lg h-10 ${width}`} onClick={onclick}>{promptTxt}</button>

  );
};
export default CustomBtn;