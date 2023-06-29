import React, { useState } from "react";

const Leaderboard = () => {
    const rry2 = DATA.items

  return (
      <div className="flex flex-col gap-8 p-4 text-center bg-gray-300">
          <div className="w-full h-1/8 justify-center content-center align-middle py-5 flex items-center flex-row bg-amber-200 ">
              WELCOME<br/>
              <span className="size">Here are the top 5 affordable prices on each item</span>
          </div>
          {rry2.map((item, index) => {
              return (
                  <div key={index} className="flex flex-col rounded-xl bg-white px-6 py-8">
                      <span className="font-extrabold text-xl text-cyan-500">{item.name}</span>
                      {item.top1 && <div className="flex justify-between font-mono">
                          <span>1</span>
                          <span>{item.top1}</span>
                          <span>{item.top1Price}</span>
                      </div>}
                      {item.top2 && <div className="flex justify-between font-mono">
                          <span>2</span>
                          <span>{item.top2}</span>
                          <span>{item.top2Price}</span>
                      </div>}
                      {item.top3 && <div className="flex justify-between font-mono">
                          <span>3</span>
                          <span>{item.top3}</span>
                          <span>{item.top3Price}</span>
                      </div>}
                      {item.top4 && <div className="flex justify-between font-mono">
                          <span>4</span>
                          <span>{item.top4}</span>
                          <span>{item.top4Price}</span>
                      </div>}
                      {item.top5 && <div className="flex justify-between font-mono">
                          <span>5</span>
                          <span>{item.top5}</span>
                          <span>{item.top5Price}</span>
                      </div>}
                  </div>
              )
          })}
      </div>
  );
};
export default Leaderboard;
