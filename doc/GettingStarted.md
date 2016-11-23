# <a name="top"></a>Getting Started

We encourage all PHYS366 students, **especially first year students**, to consider
attending all or part of the [KIPAC Computing Boot Camp](https://kipac.github.io/BootCamp/), which will have been held early on in the year.

We will be using [Jupyter Notebooks](https://jupyter.org/)
with [IPython](http://ipython.org/)
extensively in this course, so you
will need a computer that is running `linux` or `Mac OS X` and
is set up to run them. See the [Stanford README](Stanford.md) if you plan on using the Stanford-wide unix systems rather than your own system or one provided by your lab.

We will also be using the [GitHub](https://github.com) web service to
distribute course materials, including homework assignments, and to
keep track of your work - so you will need to be set up with `git` and
GitHub too.

* [Git and GitHub](#github)
* [IPython Notebooks](#ipynb)
* [Python Packages](#packages)

## <a name="github"></a>Git and GitHub

You are probably reading this file in a browser on the GitHub website.
By exploring a little you can find all the course materials for
PHYS366. Much of the material can be browsed this way, but to get everything out of the course, you will need a local copy of the repository. PHYS366 students will also need a copy of the private homework repository (see [Stanford.md](Stanford.md)).

If all this talk of "forks", "clones", "git" etc. below begins to sound scary, you might want to have a read of [this guide to getting started with git and GitHub](https://github.com/KIPAC/GettingStarted#top), and perhaps listen to Phil explaining (hopefully) everything you need to know in [this video](https://www.youtube.com/watch?v=2g9lsbJBPEs).

### Forking a repo

A fork is a copy (a "clone") of a repository, within GitHub, that belongs to you. It is not strictly necessary to fork the main course repo (you could clone it directly; see below), but PHYS366 students need to fork the homework repo before cloning it to their local systems.

While viewing the GitHub repository that you want to fork, make sure you are logged in, and you should see a button in the top righthand corner marked "Fork". Click this button. Ta-daa! You have your own copy of the repository, hosted at GitHub.

In some circumstances, it seems that GitHub will automatically have you "watching" previous forks of the repo by others. Go ahead and unwatch them, if you want to avoid the associated notifications.

### Cloning a repo

To get a repo onto your local system, you need to clone it with the command
```bash
git clone <address>
```
Here, `<address>` is the git address of the remote repo (either the original or your fork), which will be something like `git@github.com:KIPAC/StatisticalMethods.git`. You can reveal this address by clicking the "Clone or download" button on the repo's GitHub page. Give this command a try.

It will likely fail, with one of two errors. If you get a message like this:
```
Permission denied (publickey)
```
it's is because you are not yet authorized to write to files on GitHub's computers. To enable them to let you in, you just have to give them your *public SSH key*. (This is all worth it, I promise: setting this up will allow you to push and pull without typing your GitHub password all the time.) Go to the [SSH settings part of your GitHub profile](https://github.com/settings/ssh) and add a new key, pasting in the contents of your file (do "`more ~/.ssh/id_rsa.pub`". "Title" can be anything - I use "laptop".) If that file doesn't exist, you can make one with the command `ssh-keygen`. Now you should be able to interact with GitHub repositories via the command line.

Alternatively, you might get an error message because you don't have `git` installed. There are a number of ways to install `git`, and the best one will depend on your operating system. A good Google search query could be, for example, "install git Mac OS X 10.8.5".

## <a name="ipynb"></a>Jupyter Notebooks with IPython

The notebooks provided with this course are
["Jupyter"](https://jupyter.org/) notebooks,  which run IPython
version 4.0. You can read more at [the IPython
website](http://ipython.org/) but the bottom line is: you need the
latest version.

### If you have `python` already installed on your machine:

Try the following on the command line:

(Note that even if `python` is already installed, this `pip` method may not work as some packages require additional libraries that your system may not have. In such senarios, use the `conda` method below.)
```bash
pip install ipython jupyter
```
This will install IPython 4.0 from source, so may take a few minutes.

### If you do not have `python`:

Note that these instructions also work if you do have `python` installed already. This method may be preferable in any case, if you lack administrative privileges and want easy control over your `python` environment.

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
number of things you will need for this course. First of all, you'll
need to be able to run IPython 4.0 notebooks:
```bash
conda install ipython jupyter
```

### To edit and run a notebook:

In a new shell, and the top level directory of the repository, try
```bash
jupyter notebook &
```
You should see a new tab open in your web browser, and a display of your file system (starting from your current directory) appear.

**NB. It's important you launch the notebook from the top level directory of the repo (or higher), so that relative links within the repo work correctly.** If you don't do this, you will get "404" errors.
```bash
cd StatisticalMethods
jupyter notebook &
```

### If you get stuck:

Good Google search queries are "pip install jupyter" and
"miniconda install jupyter".
Also many of the KIPAC grad students have been through this before,
and can help you out if you ask them nicely.
If you still can't figure out what's going wrong, send us an [issue](https://github.com/KIPAC/StatisticalMethods/issues).


## <a name="packages"></a>Python Packages

You'll need a number of python packages available for this course.
Here's the shopping list:
```python
numpy
scipy
pandas
matplotlib
corner
astropy
mechanize
seaborn
TreeCorr
```

If you have `anaconda` or `miniconda` python, you can install these
with e.g.:
```bash
conda install astropy
```
Otherwise, or for some of these packages that are not in conda, try:
```bash
pip install astropy
```
If neither of these works for `astropy`, please
see [their website](http://astropy.readthedocs.org/en/stable/install.html)
for installation help.
