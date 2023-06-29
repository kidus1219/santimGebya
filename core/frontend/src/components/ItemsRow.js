import React from "react";
import CustomBtn from "./ CustomBtn";
import InputComponent from "./InputComponent";
import SelectComponent from "./SelectComponent";

const ItemsRow = ({options, handleChange,index, formData}) => {
  return (
    <div className="w-full px-0.5 h-1/8 rounded-xl justify-center content-center align-middle py-4 flex items-center flex-row bg-orange-100 ">

      <SelectComponent options={options} name="pk" value={formData[index].pk} onchange={(event)=> handleChange(event,index)}/>
      <InputComponent width="w-1/4" type="number" placeholder="quantity"  min={0} name="quantity" value={formData[index].quantity} onchange={(event)=> handleChange(event,index)}/>
      <InputComponent width="w-1/4"  type="number" placeholder="total price" min={0} name="price" value={formData[index].price}  onchange={(event)=> handleChange(event,index)}/>

    </div>
  );
};
export default ItemsRow;
