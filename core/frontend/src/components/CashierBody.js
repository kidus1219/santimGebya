import React, {useState} from "react";
import CustomBtn from "./ CustomBtn";
import ItemsRow from "./ItemsRow";
import SelectComponent from "./SelectComponent";
import InputComponent from "./InputComponent";
import QRCode from 'react-qr-code';



const CashierBody = () => {
    function generateQRCode(val) {
            var qrCodeCanvas = document.getElementById('qrCodeCanvas');
            qrCodeCanvas.innerHTML = '';

            var qrCode = new QRCode(qrCodeCanvas, {
                text: inputText,
                width: 128,
                height: 128
            });
        }
        const [showingQr, setShowingQr] = useState(false)
        const [incomming, setIncomming] = useState('')
        const [count,setCount]= useState(0)
        const [rowItems, addRowItems] = useState([<ItemsRow key={0} options={DATA.items}/>]);

        const [rry, setRry] = useState([1])

        const [formData, setFormData]= useState([
            {pk:'2', quantity:'',price:''}]
        )

        const addItems = () => {
            setRry(prevState => [...prevState, {quantity: 0, price: 0}])
            setFormData([...formData, {pk:'2', quantity:'',price:''}])
        }


        const handleChange= (event,index)=>{
           const updatedFormData=[...formData];
            updatedFormData[index][event.target.name]=event.target.value;
            setFormData(updatedFormData);
        }

        const handleSubmit= (event)=>{
            event.preventDefault()

            console.log("form: ",formData)
            fetch(DATA.qrApi, {
        method: "POST",
        headers: DATA.fetchHeaders,
        mode: "same-origin",
        body: JSON.stringify({ formData: formData }),
      })
        .then((resp) => resp.json())
        .then((data) => {

          if (data.signal > 0) {

                setIncomming(JSON.parse(data.msg).url)
                setShowingQr(true)
            // alert(data.msg);
            
          } else {
            alert("Failed: " + data.msg);
          }
        })
        .catch((error) => {

          alert("Something went wrong: " + error);
          console.log(error)
          // maybe alert also the status code
        });


        }
  return (
    <div className="w-full h-screen justify-start  align-middle flex flex-col items-center bg-secondary2 ">
        {showingQr && <QRCode value={incomming} size={628}/>}
        <form className="w-full h-full flex flex-col gap-4 pt-4 px-2" onSubmit={handleSubmit}>

            {rry.map((item, index) => {
                return (<ItemsRow key={index} index={index} handleChange={handleChange} formData={formData} quantity={item.quantity} price={item.price} options={DATA.items}/>)
            })}



        <div className="w-full my-2">
            <span onClick={addItems} className="bg-button text-slate-100 rounded-lg p-4">Add item</span>
            {/*<CustomBtn onclick={addItems} promptTxt="Add Item" width="w-1/2"/>*/}
        </div>
        <div className="w-full mt-auto h-1/8 justify-center   py-5 flex  flex-row self-end bg-amber-200 ">
            <CustomBtn type="submit" promptTxt="Generate QR code" width="w-3/4"/>
        </div>
        </form>

    </div>
  );
};
export default CashierBody;
