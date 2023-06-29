import React from "react";
import CustomBtn from "./ CustomBtn";

const InputComponent = ({type,placeholder, min}) => {
  return (
    <div className="w-1/4 h-1/8 justify-center content-center align-middle py-1 flex items-center flex-row  ">

        <input className="w-full mx-1" type={type} placeholder={placeholder} min={min}/>

    </div>
  );
};
export default InputComponent;
