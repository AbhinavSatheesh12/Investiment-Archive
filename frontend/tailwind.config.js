/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                'dark-bg': '#0f172a',
                'card-bg': '#1e293b',
                'primary': '#3b82f6',
                'success': '#22c55e',
                'error': '#ef4444',
            }
        },
    },
    plugins: [],
}
