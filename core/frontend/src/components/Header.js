import React from "react";
import hagurashLogo from "../../public/images/hagurash_logo_a.jpg";
const Header = ({ pageTitle, pageTitleClick, pageDesc, pageIcon, topRight }) => {
  return (
    <div className="w-full flex flex-col pt-4 pl-8 pr-12 bg-primary rounded-b-3xl text-accent">
      <div className="flex justify-between">
        <img className="" alt="logo" src={hagurashLogo} style={{ width: 80 }} />
          {topRight}
      </div>
      <div className="flex justify-between">
        <div className="flex flex-col">
          <span className="font-bold font-mono" onClick={pageTitleClick}> {pageTitle}</span>
          <span className="text-xs text-secondary2"> {pageDesc}</span>
        </div>
          <div className="absolute right-10 bg-primary text-accent border-secondary border-8 rounded-full p-2">
              {pageIcon}
          </div>
      </div>
    </div>
  );
};
export default Header;
