import React, { useState } from "react";

const Leaderboard = () => {
    const rry = [
        {'name': 'shinkurt', 'top1': 'egele', 'top1price': 55, 'top2': 'man', 'top2price':70},
        {'name': 'shinkurt', 'top1': 'egele', 'top1price': 55, 'top2': 'man', 'top2price':70},
        {'name': 'shinkurt', 'top1': 'egele', 'top1price': 55, 'top2': 'man', 'top2price':70},
    ]

  return (
      <div className="flex flex-col gap-8 p-4 text-center bg-gray-300">
          {rry.map((item, index) => {
              return (
                  <div key={index} className="flex flex-col rounded-xl bg-white px-2 py-8">
                      <span className="font-extrabold text-xl text-cyan-500">{item.name}</span>
                      {'top1' in item && <div className="flex justify-around font-mono">
                          <span>1</span>
                          <span>{item.top1}</span>
                          <span>by</span>
                      </div>}
                  </div>
              )
          })}
      </div>
  );
};
export default Leaderboard;
