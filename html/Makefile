DOCS ?= ../docs

NOTEBOOKS ?= $(shell cd .. && ls notes/*.ipynb tutorials/*.ipynb)
HTMLS ?= $(addprefix $(DOCS)/,index.html $(addsuffix .html,$(basename $(NOTEBOOKS))))

.PHONY: default

default: $(HTMLS)
#	@echo $(HTMLS)

# Note the not-foolproof translation of .ipynb to .html (for links)

# probably just the top-level index - does not need to be evaluated
$(DOCS)/%.html: %.ipynb
	jupyter nbconvert --to html $< --stdout | sed 's/.ipynb/.html/g' > $@

# notes - DO evaluate notebooks
$(DOCS)/notes/%.html: ../notes/%.ipynb
	jupyter nbconvert --to html --execute $< --stdout | sed 's/.ipynb/.html/g' > $@
	rsync --delete -vha ../notes/graphics $(DOCS)/notes/

# tutorials - DO NOT evaluate notebooks
$(DOCS)/tutorials/%.html: ../tutorials/%.ipynb
	jupyter nbconvert --to html $< --stdout | sed 's/.ipynb/.html/g' > $@
	rsync --delete -vha ../tutorials/graphics $(DOCS)/tutorials/
