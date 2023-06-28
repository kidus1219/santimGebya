import React, { useEffect } from "react";
const MainButton = ({ actors, func, text }) => {
  useEffect(() => {
    DATA.mainButton.setText(text);
    DATA.mainButton.show();
  }, []);
  useEffect(() => {
    DATA.mainButton.onClick(func);
    return () => DATA.mainButton.offClick(func);
  }, actors);

  return null;
};
export default MainButton;
