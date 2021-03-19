const colors = require('tailwindcss/colors')

module.exports = {
    purge: [
        'apps/*/templates/**/*.html',
        'apps/*/templates/**/styles/*.txt',
        'templates/**/*.html',
        'templates/**/styles/*.txt',
    ],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            colors: {
                gray: colors.trueGray,
                "red-vivid-050": "#FFE3E3",
                "red-vivid-100": "#FFBDBD",
                "red-vivid-200": "#FF9B9B",
                "red-vivid-300": "#F86A6A",
                "red-vivid-400": "#EF4E4E",
                "red-vivid-500": "#E12D39",
                "red-vivid-600": "#CF1124",
                "red-vivid-700": "#AB091E",
                "red-vivid-800": "#8A041A",
                "red-vivid-900": "#610316",
            },
            boxShadow: {
                center: 'rgb(0 0 0 / 0%) 0px 0px 0px 0px, rgb(0 0 0 / 0%) 0px 0px 0px 0px, rgb(0 0 0 / 10%) 0px 1px 3px 0px, rgb(0 0 0 / 6%) 0px 1px 2px 0px, rgb(0 0 0 / 10%) 0px -1px 3px 0px, rgb(0 0 0 / 6%) 0px -1px 2px 0px',
            },
            transitionDuration: {
                '0': '0ms',
                '2000': '2000ms',
            }
        },
    },
    variants: {
        extend: {
            textAlign: ['last'],
            backgroundColor: ['active'],
            translate: ['group-hover']
        }
    },
    plugins: [
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        require('@tailwindcss/forms'),
    ],
}
