/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        IowanOld: ["Iowan-Old"],
        IrishGrover: ["Irish-Grover"],
      },
      colors: {
        transparent: "rgba(0,0,0,0)",
        white: "#ffffff",
        black: "#000000",
        blue: "#1f32ff",
        green: "#004c4c",
        red: "#f00",
        gold: "#FFD700",
        button:"#d97706",
        secondary2: "#f8fafc",
        inactiveBtn: "#0C152D", // make the opacity only 47%

        // secondary: "#E3E3E3",
        // accent: "#0C152D",

        primary: "#ffffff",
        secondary: "#E3E3E3",
        accent: "#0E225A",
      },
    },
  },
  plugins: [],
};
