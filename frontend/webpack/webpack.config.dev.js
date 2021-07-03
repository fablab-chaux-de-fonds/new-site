const Path = require('path');
const Webpack = require('webpack');
const { merge } = require('webpack-merge');
const StylelintPlugin = require('stylelint-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const ESLintPlugin = require('eslint-webpack-plugin');

const common = require('./webpack.common.js');

module.exports = merge(common, {
  target: 'web',
  mode: 'development',
  devtool: 'inline-cheap-source-map',
  output: {
    chunkFilename: 'js/[name].chunk.js',
    filename: 'js/[name].js',
    publicPath: 'http://localhost:9091/',
  },
  devServer: {
    inline: true,
    hot: true,
    port: 9091,
    writeToDisk: true,
    headers: {
      "Access-Control-Allow-Origin": "*",
    }
  },
  plugins: [
    new Webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('development'),
    }),
    new StylelintPlugin({
      files: Path.join('src', '**/*.s?(a|c)ss'),
      fix: true,
    }),
    new MiniCssExtractPlugin({filename: 'css/app.css',}),
    new ESLintPlugin({
        fix: true,  
      }),
  ],
  module: {
    rules: [
      {
        test: /\.html$/i,
        loader: 'html-loader',
      },
      {
        test: /\.js$/,
        include: Path.resolve(__dirname, '../src'),
        loader: 'babel-loader',
      },
      {
        test: /\.s?css$/i,
        use: [MiniCssExtractPlugin.loader, 'css-loader?sourceMap=true', 'postcss-loader', 'sass-loader'],
      },
    ],
  },
});
