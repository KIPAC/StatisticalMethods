
# Doing Homework via GitHub

We'll go through these instructions on the first day of class.
[Familiarity with GitHub](https://github.com/KIPAC/StatisticalMethods/blob/master/doc/GettingStarted.md#github) will be rapidly generated and then assumed.

#### Homework Schedule:
There will be three homeworks in the 5-week course, due on Tuesdays
before class (Sept 29, Oct 6, Oct 13).


#### Accessing the homework repo:

You'll need to fork the homework repo, and clone it to your local machine.
If you cannot navigate to [the homework repository](https://github.com/drphilmarshall/PHYS366-Homework-2015) to fork it, that's because you have not been given read access to it yet. To request
this, please come and introduce yourself to your teachers and classmates
at [the sign-up issue thread](https://github.com/KIPAC/StatisticalMethods/issues/25).


#### Getting your assignments:

Notebooks containing homework assignments will be uploaded to the
[private homework
repository](https://github.com/KIPAC/PHYS366-Homework-2015)
as we go. You'll need to fork this repo, and then `git clone` to your machine so that you
can work on them.

Each week, new assignments will appear, in the "base" repository.
To get them, you will need to be able to pull directly from this repository - which
means that you need to connect to the base repo by adding it as another "remote."

To tell `git` that you want to connect to the
base repository, do:
```bash
git remote add base git@github.com:drphilmarshall/PHYS366-Homework-2015.git
```
Once you have done this, you should be able to get the latest homework assignment at any time with
```bash
git pull base master
```

#### Checking in your work:

Use `git push origin master` to keep your remote fork (whose name is "origin")
up to date as
you work through the assignment notebooks. Commit often (as soon as
the code *runs*), and push as often as possible (so that other people
can see what you're doing).

#### Submitting your work:

Homework will be graded according to the *number of solutions you are
willing to present in class*. To present, you will need to show your
work, in your edited version of the assignment notebook that you have
pushed to origin. To stake your claim, you will need to

1) Push your commits to your fork, and then _submit a `pull request`_,

2) _fill out the Google form_ (circulated with the homework) selecting which problems you have attempted, and are willing to show attempts at.

You can edit your homework submission (pull request + Google form)
any time until class starts.

Then, in the Tuesday class, for each homework problem we will draw
names at random from the list of people willing to present,  and ask
you to talk us through your solution, in your notebook (on your fork).
These attempts do not need to be complete!  You should be able to show
what approach you took, and then either what solution you got or
describe where you got stuck.
