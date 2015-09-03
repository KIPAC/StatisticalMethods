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

#### Fork the repo, and clone it to your local machine:

On the [PHYS366 GitHub repository site](https://github.com/drphilmarshall/StatisticalMethods), make sure you are logged in and you should see a button in the top righthand corner marked "Fork". Press this button.

A fork is a copy (a "clone") of a repository, that belongs to you. You can edit the files in it and run the code, either on its GitHub page, or on your local machine. 

To get your new files onto your laptop, you need to make a local copy, with:
```bash
git clone <address>
```
Here, `<address>` is the git address of your remote fork, and will have an address something like `git@github.com:USERNAME/StatisticalMethods.git` where `USERNAME` is your github username. Give this command a try.

> It will likely fail, with one of two errors. If you get a message like this:
```
Permission denied (publikey)
```
it's is because you are not yet authorized to write to files on GitHub's computers. To enable them to let you in, you just have to give them your *public SSH key*. (This is all worth it, I promise: setting this up will allow you to push and pull without typing your GitHub password all the time.) Go to the [SSH settings part of your GitHub profile](https://github.com/settings/ssh) and add a new key, pasting in the contents of your file (do "`more ~/.ssh/id_rsa.pub`". "Title" can be anything - I use "laptop".) If that file doesn't exist, you can make one with the command `ssh-keygen`. Now you should be able to interact with GitHub repositories via the command line.

> Alternatively, you might get an error message because you don't have `git` installed. There are a number of ways to install `git`, and the best one will depend on your operating system. A good Google search query could be, for example, "install git Mac OS X 10.8.5".


#### Edit the notebooks, and check in your work:

Your local clone is connected to your "remote" fork at GitHub: `git` knows where you cloned your repository from, and names it "origin." If a file changes on the GitHub site (e.g. because you edited it there directly), you can get that latest version with `git pull origin master`. Likewise, if you edit a file locally, you can bring your remote fork up to date with `git push origin master`. New files have to be added to the local repository with `git add <filename>` and then edits saved ("checked in" or "committed") with `git commit -m "Some brief but informative commentary" <filename>` Commit often (as soon as the code *runs*), and push as often as possible (so that other people can see what you're doing). 

