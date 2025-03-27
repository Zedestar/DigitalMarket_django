module.exports = {
  content: [
    "./templates/*.html", // Scan all HTML files directly inside 'templates/'
    "./*/templates/**/*.html", // Scan HTML files inside all Django apps' 'templates/' folders
    "./static/tailwind/**/*.css", // Scan all Tailwind CSS files inside 'static/tailwind/'
    "./static/**/*.js", // Scan JS files (if Tailwind classes are used in JS)
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
