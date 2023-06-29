import React, { useState } from "react";
import CashierHeader from "../components/CashierHeader"
import { AiOutlineLogin } from "react-icons/ai";
import { RiLockPasswordFill } from "react-icons/ri";
import Header from "../components/Header";
import Footer from "../components/Footer";
import MainButton from "../components/MainButton";
import CashierBody from "../components/CashierBody";
import InputComponent from "../components/InputComponent";
import ItemsRow from "../components/ItemsRow";
import CustomBtn from "../components/ CustomBtn";

const Profile = ({merchant_id,store_name,store_location}) => {

    const [formData, setFormData]= useState(
            {store_name:'', store_location:''}
        );
     const handleChange= (event)=>{
            setFormData((prevState)=> ({...prevState, [event.target.name]: event.target.value}))
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        // Do something with the form data, such as sending it to a server or updating the component's state
        console.log("profile form",formData);
    };
  return (
      <div className="flex flex-col w-full h-screen text-center bg-gray-300">
             <div className="w-full h-1/8 justify-center content-center align-middle py-5 flex items-center flex-row bg-amber-200 ">
                 Merchant ID:
                <span className="text-sky-600 flex items-center mx-2 ">{merchant_id}</span>
            </div>
            <div className="w-full h-full justify-start  align-middle flex flex-col items-center bg-secondary2 ">
                <form className="w-full h-full  flex flex-col gap-4  content-center"  onSubmit={handleSubmit}>
                    <label htmlFor="store_name" className="mt-6">Store Name</label>
                    <InputComponent width="w-3/4" type="text" placeholder="Store name"  min={0} name="store_name" value={formData.store_name} onchange={(event)=> handleChange(event)}/>
                    <label htmlFor="store_location">Store Location</label>
                    <InputComponent width="w-3/4"  type="text" placeholder="Store Location" min={0} name="store_location" value={formData.store_location}  onchange={(event)=> handleChange(event)}/>

                    <div className="w-full  h-1/8 mt-auto justify-center   py-5 flex  flex-row self-end bg-amber-200 ">
                        <CustomBtn type="submit" promptTxt="Update Mercant Data" width="w-3/4"/>
                    </div>
                </form>
            </div>

      </div>
  );
};
export default Profile;
