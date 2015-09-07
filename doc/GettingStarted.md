# <a name="top"></a>Getting Started

We will be using [IPython Notebooks](http://ipython.org/notebook.html)
extensively in this course, so you
will need a computer that is running `linux` or `Mac OS X` and
is set up to run them. Ideally you have a laptop, since there will be in-class activities - otherwise you will need to share (in-class projects will generally be in groups in any case). If you do not have a laptop or a desktop that can run the required software, see below for information about the Stanford-wide unix systems.

We will also be using the [GitHub](https://github.com) web service to
distribute course materials, including homework assignments, and to
keep track of your work - so you will need to be set up with `git` and
GitHub too.

* [IPython Notebooks](#ipynb)
* [Python Packages](#packages)
* [Git and GitHub](#github)
* [Homework](#homework)
* [Textbooks](#textbooks)
* [Stanford unix systems](#stanfordunix)

-----

### <a name="ipynb"></a>IPython Notebooks

#### If you have `python` already installed on your machine:

Try the following on the command line:
```bash
pip install "ipython[notebook]"
```
This will install IPython from source, so may take a few minutes.

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
number of things you will need for this course. First of all, you'll
need to be able to run IPython notebook:
```bash
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

[Back to top.](#top)

-----

### <a name="packages"></a>Python Packages

You'll need a number of python packages available for this course.
Here's the shopping list:
```python
numpy
scipy
pandas
matplotlib
astropy
```

If you have `anaconda` or `miniconda` python, you can install these
with e.g.:
```bash
conda install astropy
```
Otherwise, try:
```bash
pip install astropy
```
If neither of these works for `astropy`, please
see [their website](http://astropy.readthedocs.org/en/stable/install.html)
for installation help.

[Back to top.](#top)

-----

### <a name="github"></a>Git and GitHub

You are probably reading this file in a browser on the GitHub website.
By exploring a little you can find all the course materials for
PHYS366. Some of them are IPython Notebooks that you will need in
class for various exercises. Meanwhile, your homework assignments will
be made available at [this private
repository](https://github.com/drphilmarshall/PHYS366-Homework-2015)
You will need local copies of both these repos to be able to do the
course work.

#### Fork the main repo, and clone it to your local machine:

On the [PHYS366 GitHub repository site](https://github.com/drphilmarshall/StatisticalMethods), make sure you are logged in and you should see a button in the top righthand corner marked "Fork". Press this button.

A fork is a copy (a "clone") of a repository, that belongs to you. You can edit the files in it and run the code, either on its GitHub page, or on your local machine. (If all this talk of "forks", "clones", "git" etc is beginning to sound scary, you might want to have a read of [this guide to getting started with git and GitHub](https://github.com/drphilmarshall/GettingStarted#top).)

To get your new files onto your laptop, you need to make a local copy, with (on the command line):
```bash
git clone <address>
```
Here, `<address>` is the git address of your remote fork, and will have an address something like `git@github.com:USERNAME/StatisticalMethods.git` where `USERNAME` is your GitHub username. Give this command a try.

> It will likely fail, with one of two errors. If you get a message like this:
```
Permission denied (publickey)
```
it's is because you are not yet authorized to write to files on GitHub's computers. To enable them to let you in, you just have to give them your *public SSH key*. (This is all worth it, I promise: setting this up will allow you to push and pull without typing your GitHub password all the time.) Go to the [SSH settings part of your GitHub profile](https://github.com/settings/ssh) and add a new key, pasting in the contents of your file (do "`more ~/.ssh/id_rsa.pub`". "Title" can be anything - I use "laptop".) If that file doesn't exist, you can make one with the command `ssh-keygen`. Now you should be able to interact with GitHub repositories via the command line.

> Alternatively, you might get an error message because you don't have `git` installed. There are a number of ways to install `git`, and the best one will depend on your operating system. A good Google search query could be, for example, "install git Mac OS X 10.8.5".

[Back to top.](#top)


#### <a name="homework"></a>Fork the homework repo, and clone it to your local machine:

If you cannot navigate to [the homework repository](https://github.com/drphilmarshall/PHYS366-Homework-2015) to fork it,
that's because you have not been given read access to it yet. To request
this, please come and introduce yourself to your teachers and classmates
at [the sign-up issue thread](https://github.com/drphilmarshall/StatisticalMethods/issues/25).

#### Edit the notebooks, and check in your work:

Each of your local clones is connected to your corresponding
"remote" fork at GitHub: `git` knows where you cloned your repository from, and names it "origin." If a file changes on the GitHub site (e.g. because you edited it there directly), you can get that latest version with `git pull origin master`. Likewise, if you edit a file locally, you can bring your remote fork up to date with `git push origin master`. New files have to be added to the local repository with `git add <filename>` and then edits saved ("checked in" or "committed") with `git commit -m "Some brief but informative commentary" <filename>` Commit often (as soon as the code *runs*), and push as often as possible (so that other people can see what you're doing).

[Back to top.](#top)

-----

### <a name="textbooks"></a>Textbooks

This course will be mostly self-contained, but it's good to read around the subject (and you might find clues to some of the exercises while you're at it). We recommend the following textbooks to accompany this course:

* **[Ivezic et al “Statistics, Data Mining and Machine Learning in Astronomy”](http://www.astroml.org/)**

> This is a very useful "cookbook," providing easy-to-follow recipes in astronomical data analysis and good, clear explanations. The library has a few copies that you can borrow, as do the course teachers - but it's
also a [good one to invest in](http://www.amazon.com/Statistics-Mining-Machine-Learning-Astronomy/dp/0691151687).

* **[MacKay “Information Theory, Inference and Learning Algorithms”](http://www.inference.phy.cam.ac.uk/mackay/itprnn/book.html)**

> This book goes way beyond the scope of PHYS366, but it's introduction to Bayesian inference is excellent, and it's free to download from the above website. You can also click through to an online bookseller from there
if you like.


Other good books to check out:

* **Gelman et al “Bayesian Data Analysis”**

> Should be available from the library, or [for online purchase here](http://www.amazon.com/Bayesian-Analysis-Chapman-Statistical-Science/dp/1439840954/).

[Back to top.](#top)

-----

### <a name="stanfordunix"></a>Stanford unix systems

See the information on unix systems accessible to all students [here](https://itservices.stanford.edu/service/sharedcomputing), including the Getting Started if you are unfamiliar with unix. Note that the appropriate cluster to use is `corn` (interactive use, including compute-intensive tasks). These systems have `git` and `python` installed, but appear to have an old version of `notebook`, so you should follow the instructions above for installing `miniconda` and the required `python` packages within your home space.

[Back to top.](#top)
