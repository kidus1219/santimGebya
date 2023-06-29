import React from "react";
import hagurashLogo from "../../public/images/hagurash_logo_a.jpg";
import CustomBtn from "./ CustomBtn";
const CashierHeader = ({merchant_id}) => {
  return (
    <div className="w-full h-1/8 justify-center content-center align-middle py-5 flex items-center flex-row bg-amber-200 ">
        Merchant ID:
        <div className="text-sky-600 flex items-center mx-2 ">{merchant_id}</div>
        {/*<CustomBtn promptTxt="Edit Profile" width="w-4/12"/>*/}

    </div>
  );
};
export default CashierHeader;
