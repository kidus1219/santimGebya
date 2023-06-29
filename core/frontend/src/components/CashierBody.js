import React, {useState} from "react";
import CustomBtn from "./ CustomBtn";
import ItemsRow from "./ItemsRow";
import SelectComponent from "./SelectComponent";
import InputComponent from "./InputComponent";



const CashierBody = () => {

        const [rowItems, addRowItems] = useState([<ItemsRow options={DATA.items} />]);

        const addItems= ()=>{
            addRowItems([...rowItems, <ItemsRow options={DATA.items} />])
        }

        const generateQR= ()=>{
            console.log("generating...")
        }

  return (
    <div className="w-full h-screen justify-start  align-middle flex flex-col items-center bg-secondary2 ">
        <div className="w-full px-px-1 h-1/8 justify-center content-center align-middle py-2 flex items-center flex-row bg-button ">
            <div className="w-1/4 justify-center content-center align-middle py-0.5 flex items-center flex-row font-bold text-black">
                Item Name
            </div>
            <div className="w-1/4 justify-center content-center align-middle py-0.5 flex items-center flex-row font-bold text-black">
                Quantity
            </div>
            <div className="w-1/4 justify-center content-center align-middle py-0.5 flex items-center flex-row font-bold text-black">
                Total Price
            </div>
      </div>
        <form className="w-full h-3/4">
            {
                rowItems.map(
                    row =>{
                        return(
                           <ItemsRow key={index} options={DATA.items}/>
                        )
                    }
                )
            }

        <div className="w-full my-2">
            <CustomBtn onclick={addItems} promptTxt="Add Item" width="w-1/2"/>
        </div>

        </form>
        <div className="w-full  h-1/8 justify-center   py-5 flex  flex-row self-end bg-amber-200 ">
            <CustomBtn onclick={generateQR}promptTxt="Generate QR code" width="w-3/4"/>
        </div>
    </div>
  );
};
export default CashierBody;
