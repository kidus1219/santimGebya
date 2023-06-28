const { join } = require("path");

module.exports = {
  entry: {
    // login: join(__dirname, "src", "login.js"),
    profile: join(__dirname, "src", "profile.js"),
    // store: join(__dirname, "src", "store.js"),
    // orders: join(__dirname, "src", "orders.js"),
  },
  output: {
    filename: "[name].js", //do hasch chaching here somehting like [hash][ext]
    path: join(__dirname, "../static/customer", "js"),
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: { presets: ["@babel/preset-env", "@babel/preset-react"] },
      },
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader", "postcss-loader"],
      },
      {
        test: /\.(jpg|png|jpeg)/i,
        type: "asset/resource",
        generator: {
          filename: "../image/[hash][ext]", // TODO what is this
        },
      },
      {
        test: /\.(ttf|otf|woff|woff2|gxf)/i,
        type: "asset/resource",
        generator: {
          filename: "../font/[hash][ext]", // TODO what is this
        },
      },
    ],
  },
  //    devtool: "source-map",
};
