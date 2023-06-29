import React from "react";
import CustomBtn from "./ CustomBtn";

const InputComponent = ({width,type,placeholder, min, name, value, onchange}) => {
  return (
    <div className={`${width} h-1/8 justify-center self-center content-center align-middle py-1 flex items-center flex-row  `}>

        <input className="w-full mx-1 self-center" name={name} value={value} onChange={onchange} type={type} placeholder={placeholder} min={min} required/>

    </div>
  );
};
export default InputComponent;
