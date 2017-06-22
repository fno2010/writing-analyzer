ENGINE    := xelatex
FILENAME  := paper
WORDCOUNT := count.html

all: pdf
	texcount -sub=section -html $(FILENAME).tex > $(WORDCOUNT)

tex:
	pandoc --template=elsevier.xelatex --natbib -o $(FILENAME).tex $(FILENAME).md

pdf: tex
	$(ENGINE) $(FILENAME)
	bibtex $(FILENAME)
	$(ENGINE) $(FILENAME)
	$(ENGINE) $(FILENAME)

clean:
	rm -f *.dvi *.aux *.log *.bbl *.blg *.spl

dist-clean: clean
	rm -f *.tex *.pdf
