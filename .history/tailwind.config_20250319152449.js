module.exports = {
  content: [
    "./templates/*.html", // Django base template and others
    "./**/**/*.html", // Django app templates
    // "./static/js/**/*.js", // Your JS files
    "./static/*.css", // Any CSS files
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
