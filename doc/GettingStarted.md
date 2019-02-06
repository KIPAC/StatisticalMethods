# <a name="top"></a>Getting Started

We encourage all PHYS366 students, especially first year students, to
attend all or part of the [KIPAC Computing Boot Camp](https://kipac.github.io/BootCamp/), which is held at the beginning of the academic year.

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
* [Guidlines for Keeping Notebooks in Git](#gitnote)

## <a name="github"></a>Git and GitHub

You are probably reading this file in a browser on the GitHub website.
By exploring a little you can find all the course materials for
PHYS366. Much of the material can be browsed this way, but to get everything out of the course, you will need a local copy of the repository. PHYS366 students will also need a copy of the private homework repository (see [Stanford.md](Stanford.md)).

If all the talk of "forks", "clones", "git" etc. below begins to sound scary, you might want to have a read of [this guide to getting started with git and GitHub](https://github.com/KIPAC/GettingStarted#top), and perhaps listen to Phil explaining (hopefully) everything you need to know in [this video](https://www.youtube.com/watch?v=2g9lsbJBPEs).

### Forking a repo

A fork is a copy (a "clone") of a repository, within GitHub, that belongs to you.
It is not strictly necessary to fork the main course repo: if you don't plan to suggest any changes to the material, you can just clone it directly as described below. But if you want to make a fork, follow these directions.

While viewing the GitHub repository that you want to fork, make sure you are logged in, and you should see a button in the top righthand corner marked "Fork".
Click this button.
Ta-daa!
You have your own copy of the repository, hosted at GitHub.

In some circumstances, it seems that GitHub will automatically have you `Watching` previous forks of the repo by others.
Go ahead and `Unwatch` them if you want to avoid the associated notifications.

### Cloning a repo

To get a repo onto your local system, you need to clone it with the shell command
```bash
git clone <address>
```
Here, `<address>` is the git address of the remote repo (either the original or your fork), which will be something like `git@github.com:KIPAC/StatisticalMethods.git`. You can reveal this address by clicking the "Clone or download" button on the repo's GitHub page. Give this command a try.

It will likely fail, with one of two errors. If you get a message like this:
```
Permission denied (publickey)
```
it's is because you are not yet authorized to write to files on GitHub's computers. To enable them to let you in, you just have to give them your *public SSH key*. (This is all worth it, I promise: setting this up will allow you to push and pull without typing your GitHub password all the time. However, if you somehow never plan to push anything to GitHub, it's simpler to clone using https rather than SSH; this does not require setting up a key.) Go to the [SSH settings part of your GitHub profile](https://github.com/settings/ssh) and add a new key, pasting in the contents of your file (do "`more ~/.ssh/id_rsa.pub`". "Title" can be anything - I use "laptop".) If that file doesn't exist, you can make one with the command `ssh-keygen`. Now you should be able to interact with GitHub repositories via the command line.

Alternatively, you might get an error message because you don't have `git` installed. There are a number of ways to install `git`, and the best one will depend on your operating system. A good Google search query could be, for example, "install git Mac OS X 10.8.5".

If all else fails, note that you can download a GitHub repository as a `zip` file also.
However, this is a simple, one-time download, meaning that there is no way to get updates other than to re-download the entire repository - so we recommend cloning the repo, if at all possible.

## <a name="ipynb"></a>Jupyter Notebooks with IPython

The notebooks provided with this course are
["Jupyter"](https://jupyter.org/) notebooks,  which run IPython. You can read more at [the IPython
website](http://ipython.org/) but the bottom line is: you should get the
latest version, just to be safe.

### If you have `python` already installed on your machine:

Try the following on the command line:
```bash
pip install ipython jupyter
```
This will install the current IPython from source, so may take a few minutes.

Note that even if `python` is already installed, this `pip` method may not work as some packages require additional libraries that your system may not have. In such senarios, use the `conda` method below.

Also note that there are some limitations to the `python` that comes pre-installed on OS X systems. It is almost certainly worth it (and safe!) to install and use Miniconda instead.

### If you do not have `python`:

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
need to be able to run Jupyter notebooks:
```bash
conda install ipython jupyter
```

Note that the above instructions also work if you do have `python` installed already. This method may be preferable in any case, if you lack administrative privileges and want easy control over your `python` environment.

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

### Viewing the notebooks as slides

We use the [RISE jupyter IPython slideshow extension](https://github.com/damianavila/RISE) to display notebook cells as slides. To do likewise (although you don't really need to), you would need to install RISE, following the instructions in the [RISE README](https://github.com/damianavila/RISE).


### If you get stuck:

Good Google search queries are "pip install jupyter" and
"miniconda install jupyter".
Also many of the KIPAC grad students have been through this before,
and can help you out if you ask them nicely.
If you still can't figure out what's going wrong, send us an [issue](https://github.com/KIPAC/StatisticalMethods/issues).

### If you are completely new to Python

We recommend checking out the Python [tutorial](https://docs.python.org/3/tutorial/index.html). You will also appreciate the documentation for the [Python standard library](https://docs.python.org/3/library/index.html), [NumPy](https://docs.scipy.org/doc/numpy/reference/) and [SciPy](https://docs.scipy.org/doc/scipy/reference/).

## <a name="packages"></a>Python Packages

You'll need a number of python packages in this course.
The shopping list is given in the [`requirements.txt`](https://github.com/KIPAC/StatisticalMethods/blob/master/requirements.txt) file.

If you have `anaconda` or `miniconda` python, you can try installing these with e.g.:
```bash
conda install astropy
```
Otherwise, or for some of these packages that are not in conda, try:
```bash
pip install corner
```

If neither of these methods works for `astropy`, please
see [their website](http://astropy.readthedocs.org/en/stable/install.html)
for installation help.

Some additional packages that may be useful at some point are listed in [MCMC_packages.md](MCMC_packages.md). These can be installed if you need them with `pip` or `conda`.


## <a name="gitnote"></a>Guidelines for Keeping Notebooks in Git

This section is mainly a reminder for us, but might also be useful information for those hoping to avoid conflicts when git pulling (e.g. from the base repo) and pushing (to your fork).

Jupyter notebooks are fundamentally a text-based format, and thus relatively straightforward to difference between versions. This breaks down when graphics are embedded within a notebook, however. In general, cell outputs are more difficult to difference than "clean" notebooks, although purely text outputs shouldn't be too bad.

To minimize the possibility of conflicts, we will attempt to obey the following rule ourselves: *Only check in notebooks that have been cleared of all outputs.* Static images may still be included via html within markdown, but any interactively produced graphics or text outputs will be missing.

We will also endeavor not to update or fix notebooks once they have been covered in class, in case people have been taking notes in their local copies. In principle, this should not cause any problems as long as your notes are added in separate cells (and we abide by the italicized rule above). To be safe, however, *we recommend that students not take notes in the original version-controlled file* - either make a copy or take notes some other way. This is especially true given that individual files may change significantly or even disappear from year to year.

If, despite all efforts, you end up with conflicts for individual files when trying to pull, you can try the following

1. Make a copy of your version of the offending file.
2. Run `git checkout -- <filename>` to revert `filename` to its state the last time you pulled.

In the worst case, there's always the [XKCD method](https://xkcd.com/1597/): rename the StatisticalMethods folder to something else, and clone a fresh copy of the repo from GitHub.
