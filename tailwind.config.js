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
                // "gray-050": "#F0F4F8",
                // "gray-100": "#D9E2EC",
                // "gray-200": "#BCCCDC",
                // "gray-300": "#9FB3C8",
                // "gray-400": "#829AB1",
                // "gray-500": "#627D98",
                // "gray-600": "#486581",
                // "gray-700": "#334E68",
                // "gray-800": "#243B53",
                // "gray-900": "#102A43",
                gray: colors.trueGray,
                'gray-050': colors.trueGray['50'],
                "red-050": "#FFE3E3",
                "red-100": "#FFBDBD",
                "red-200": "#FF9B9B",
                "red-300": "#F86A6A",
                "red-400": "#EF4E4E",
                "red-500": "#E12D39",
                "red-600": "#CF1124",
                "red-700": "#AB091E",
                "red-800": "#8A041A",
                "red-900": "#610316",
                "purple-050": "#F2EBFE",
                "purple-100": "#DAC4FF",
                "purple-200": "#B990FF",
                "purple-300": "#A368FC",
                "purple-400": "#9446ED",
                "purple-500": "#8719E0",
                "purple-600": "#7A0ECC",
                "purple-700": "#690CB0",
                "purple-800": "#580A94",
                "purple-900": "#44056E",
                "blue-050": "#E3F8FF",
                "blue-100": "#B3ECFF",
                "blue-200": "#81DEFD",
                "blue-300": "#5ED0FA",
                "blue-400": "#40C3F7",
                "blue-500": "#2BB0ED",
                "blue-600": "#1992D4",
                "blue-700": "#127FBF",
                "blue-800": "#0B69A3",
                "blue-900": "#035388",
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
