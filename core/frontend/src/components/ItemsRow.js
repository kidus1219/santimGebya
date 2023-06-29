import React from "react";
import CustomBtn from "./ CustomBtn";
import InputComponent from "./InputComponent";
import SelectComponent from "./SelectComponent";

const ItemsRow = ({options}) => {
  return (
    <div className="w-full px-0.5 h-1/8 justify-center content-center align-middle py-2 flex items-center flex-row bg-orange-100 ">

      <SelectComponent options={options}/>
      <InputComponent type="number" placeholder="quantity" min={0}/>
      <InputComponent type="number" placeholder="total price" min={0}/>

    </div>
  );
};
export default ItemsRow;
