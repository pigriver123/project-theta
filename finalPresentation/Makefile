.PHONY: all clean

all: clean finalPresentation.pdf

clean:
	rm -f finalPresentation.pdf

finalPresentation.pdf: *.md
	pandoc -t beamer -s 0*.md -o finalPresentation.pdf
