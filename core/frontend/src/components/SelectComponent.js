import React from "react";
import CustomBtn from "./ CustomBtn";

const SelectComponent = ({options, name, value,onchange}) => {
  return (
    <div className="w-1/4 h-1/8 justify-center content-center align-middle py-1 flex items-center flex-row  ">
        <select name={name} onChange={onchange} value={value}>{
            options.map(
                (option, index) => <option key={index} value={option.pk}>{option.name}</option>)
        }
        </select>
    </div>
  );
};
export default SelectComponent;
