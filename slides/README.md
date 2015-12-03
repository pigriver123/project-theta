# Slides

* http://pandoc.org/demo/example9/producing-slide-shows-with-pandoc.html

## Progress report presentation

Use the above guide (link) to learn how to use pandoc with beamer to produce
slides.  I've made a template `progress.md` for you to modify.  I've also
added a `Makefile` with some recipes to build your slides and delete the
generated files.

## Final report presentation

Create a new file `final.md` and add appropriate entries to the `Makefile`.

## Instructions

### Building the slides

`make` to clean and build both progress and final slides
`make final` to build the final slides
`make progress` to build the progress slides

### Making the slides

- To edit progress slides, edit `progress.md` directly
- To edit final slides, edit each invidual portion beginning with `0X_`, where
`X` is the section number. To add a section, format each markdown file to begin
with `0X_`. For example, the 7th section can be `07_acknowledgment.md`.