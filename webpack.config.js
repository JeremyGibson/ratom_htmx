const webpack = require('webpack');
const path = require('path');

module.exports = {
    bail: true,
    mode: 'none',
    context: __dirname,
    entry: ['./ratom_htmx/assets/js/webpack_entry.js'],
    resolve: {
        extensions: ['*', '.js'],
    },
    output: {
        path: path.resolve('./ratom_htmx/static/js'),
        filename: 'main.js',
    },
    module: {
        rules: [
            {
                test: /\.(js)$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            }
        ]
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
        }),
    ]
};


