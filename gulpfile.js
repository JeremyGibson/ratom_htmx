const gulp = require("gulp");
const rename = require("gulp-rename");
const webpack = require("webpack-stream");

gulp.task('javascript', function() {
  return gulp
    .src("./ratom_htmx/assets/js/webpack_entry.js")
    .pipe(webpack(require("./webpack.config.js")))
    .pipe(rename("main.js"))
    .pipe(gulp.dest("./ratom_htmx/static/js/"));
});

gulp.task('watch-js', function(done) {
  gulp.watch(["./apps/ratom_htmx/assets/js/**/*.js"], gulp.series("javascript"));
  done();
})



gulp.task('styles', function() {
  const postcss = require("gulp-postcss");
  const tailwindcss = require("tailwindcss");

  return gulp
    .src("./ratom_htmx/assets/styles/tailwind_entry.css")
    .pipe(
      postcss([
        require("postcss-import"),
        require("postcss-preset-env"),
        tailwindcss("./tailwind.config.js"),
        require("autoprefixer"),
      ])
    )
    .pipe(rename("main.css"))
    .pipe(gulp.dest("./ratom_htmx/static/css/"));
});

gulp.task('watch-css', function(done) {
  gulp.watch(
    [
      './apps/ratom_htmx/**/*.css',
      './tailwind.config.js'
    ], gulp.series('styles')
  )
  done();
});




exports.default = gulp.series('styles', 'javascript', 'watch-css', 'watch-js');