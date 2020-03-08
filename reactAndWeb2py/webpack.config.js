const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
var webpack = require('webpack');

module.exports = {
  // Evaluate source maps
  devtool: 'source-map',

  // webpack will take the files from ./static/src/index
  entry: {
    app: './static/src/index.tsx'
  },

  // and output it into /dist as bundle.js
  output: {
    path: path.join(__dirname, '/static'),
    filename: 'bundle.js',
    sourceMapFilename: "[file].map"
  },

  // adding .ts and .tsx to resolve.extensions will help babel look for .ts and .tsx files to transpile
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.css', '.json']
  },

  module: {
    rules: [

      // we use babel-loader to load our jsx and tsx files
      {
        test: /\.(ts|js)x?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        },
      },

      // css-loader to bundle all the css files into one file and style-loader to add all the styles  inside the style tag of the document
      {
        test: /\.css$/,
        use: [
          'style-loader',
          {
            loader: 'css-loader',
            options: {
              url: false
            }
          }
        ]
      },

      {
        include: [path.resolve(__dirname, 'app'), path.resolve('js')/*, path.resolve('node_modules/preact-compat/src')*/],
        loader: 'babel-loader',
        options: {
          presets: ['react', 'es2015']
        },
        exclude: [path.resolve(__dirname, 'app/components'), path.resolve(__dirname, 'node_modules')]
      }

    ]
  },
  plugins: [
    new webpack.LoaderOptionsPlugin({
      debug: true
    })
  ],
  devServer: {
    publicPath: '/static/',
    open: true, 
    openPage: 'static/preview.html' 
  }
};
