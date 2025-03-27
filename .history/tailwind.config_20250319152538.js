module.exports = {
  content: [
    "./templates/*.html", // Django base template and others
    "./**/templates/**/*.html", // Django app templates
    "./static/*.css", // Any CSS files
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
