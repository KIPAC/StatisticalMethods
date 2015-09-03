## Getting Started

We will be using [IPython Notebooks](http://ipython.org/notebook.html)
extensively in this course, so you
will need a laptop computer that is running `linux` or `Mac OS X` and
is set up to run them.

We will also be using the [GitHub](https://github.com) web service to
distribute course materials, including homework assignments, and to
keep track of your work - so you will need to be set up with `git` and
GitHub too.

### IPython Notebooks

#### If you have `python` already installed on your machine:

Try the following on the command line:
```bash
pip install "ipython[notebook]"
```
This will install IPython from source, so may take a few minutes. 

#### If that fails (or you don't have `pip`):

You may be able to manually install each of the packages underlying notebook using some other tool, e.g.
```bash
easy_install pyzmq
```
Do this for the whole list of dependencies [here](http://ipython.org/ipython-doc/stable/install/install.html#dependencies-for-the-ipython-html-notebook).

#### If you do not have `python`:

The fastest way to get set up is with
[`Miniconda`](http://conda.pydata.org/miniconda.html). Download and run
the installer from that link, with, e.g. (on the command line)
```bash
bash Miniconda-3.6.0-MacOSX-x86_64.sh
```
Then try:
```bash
conda update conda
```
`conda` is the package manager command, and can be used to install a
number of things you will need for this course:
```bash
conda install numpy
conda install scipy
conda install pandas
conda install matplotlib
conda install ipython-notebook
```

#### To edit and run a notebook:

In a new shell, try
```bash
ipython notebook &
```
You should see a new tab open in your web browser, and a display of your file system (starting from your current directory) appear. 


#### If you get stuck:

Good Google search queries are "pip install ipython notebook" and
"miniconda install ipython notebook".
Also many of the KIPAC grad students have been through this before,
and can help you out if you ask them nicely.
If you still can't figure out what's going wrong, send us an [issue](https://github.com/drphilmarshall/StatisticalMethods/issues).

-----

### git and GitHub

You are probably reading this file in a browser on the GitHub website.
By exploring a little you can find all the course materials for
PHYS366. Some of them are IPython Notebooks that you will need in class
for various exercises, and others are stubs that will be used in
homework assignments. You need a local copy of all of this stuff to be
able to do the course work. 
