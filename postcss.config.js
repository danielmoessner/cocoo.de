const cssnano = require('cssnano')
const autoprefixer = require('autoprefixer');
const purgecss = require('@fullhuman/postcss-purgecss')

module.exports = ({env}) => ({
    plugins: [
        require("postcss-import"),
        require("postcss-nested"),
        require("tailwindcss"),
        env === 'production' ? autoprefixer() : null,
        env === 'production' ? cssnano({
            preset: ["default", {discardComments: {removeAll: true}}],
        }) : null,
    ],
})
