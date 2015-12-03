.PHONY: all clean final progress

all: clean final progress

clean:
	rm -f progress.pdf final.pdf 

final: 0*.md
	pandoc -t beamer -s 0*.md -o final.pdf

progress: progress.md
	pandoc -t beamer -s progress.md -o progress.pdf
