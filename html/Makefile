DOCS ?= ../docs
SOLS ?= ../docs/solved


NOTEBOOKS1 ?= $(shell cd .. && ls notes/*.ipynb)
NOTEBOOKS2 ?= $(shell cd .. && ls tutorials/*.ipynb)
HTMLS ?= $(addprefix $(DOCS)/,index.html $(addsuffix .html,$(basename $(NOTEBOOKS1) $(NOTEBOOKS2))))
MOREHTMLS ?= $(addprefix $(SOLS)/,$(addsuffix .html,$(basename $(NOTEBOOKS2))))

.PHONY: default

default: $(HTMLS) $(MOREHTMLS) $(DOCS)/requirements.txt
#	@echo $(HTMLS)

# Note the not-foolproof translation of .ipynb to .html (for links)

# probably just the top-level index - does not need to be evaluated
$(DOCS)/%.html: %.ipynb
	jupyter nbconvert --to html $< --stdout | sed 's/.ipynb/.html/g' > $@
# index is a special case, in fact
tmp_index.html: index.ipynb
	jupyter nbconvert --to html $< --stdout | sed 's/.ipynb/.html/g' > $@
$(DOCS)/index.html: tmp_index.html dependency_graph.html
	sed '/<h3 id="Flowchart">/rdependency_graph.html' $< > $@

# notes - DO evaluate notebooks
$(DOCS)/notes/%.html: ../notes/%.ipynb
	jupyter nbconvert --to html --execute $< --stdout | sed 's/.ipynb/.html/g' > $@
	rsync --delete -vha ../notes/graphics $(DOCS)/notes/

# unevaluated tutorials
$(DOCS)/tutorials/%.html: ../tutorials/%.ipynb
	jupyter nbconvert --to html $< --stdout | sed 's/.ipynb/.html/g' > $@
	rsync --delete -vha ../tutorials/graphics $(DOCS)/tutorials/

# evaluated tutorials
$(SOLS)/tutorials/%.html: ../tutorials/%.ipynb
	jupyter nbconvert --to html --execute $< --stdout | sed 's/.ipynb/.html/g' > $@
	rsync --delete -vha ../tutorials/graphics $(SOLS)/tutorials/

# requirements/whatever
$(DOCS)/%.txt: ../%.txt
	cp $< $@

# inter-tutorial dependences
$(SOLS)/tutorials/mcmc_diagnostics.html: $(SOLS)/tutorials/toy_photometry_gibbs.html $(SOLS)/tutorials/toy_photometry_metro.html

