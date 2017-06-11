var path = require('path');

module.exports = {
  entry : {
    mapBundle : './frontend/map.js',
    uploadBundle : './frontend/upload.js'
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
      }, {
        test: /\.scss$/,
        loaders: ['style-loader', 'css-loader', 'sass-loader']
      }
    ]
  },
  // devtool: 'source-maps',
  resolve: {
    extensions: [".js", "*"]
  }
};
