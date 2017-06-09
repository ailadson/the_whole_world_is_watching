var path = require('path');

module.exports = {
  entry : {
    mapBundle : './frontend/map.js',
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'public', 'js')
  },
  module: {
    loaders: [
      {
        test: [/\.jsx?$/, /\.js?$/],
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015']
        }
      }
    ]
  },
  devtool: 'source-maps',
  resolve: {
    extensions: [".js", "*"]
  }
};
