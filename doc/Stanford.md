# Information for Stanford Students

From the course handbook:
```
PHYSICS 366: Special Topics in Astrophysics: Statistical Methods

Existing and emerging statistical techniques and their application to astronomical surveys and cosmological data analysis. Topics covered will include statistical frameworks (Bayesian inference and frequentist statistics), numerical methods including Markov Chain Monte Carlo, and machine learning applied to classification and regression. Hands on activities based on open-source software in python. Recommended prerequisites: PHYSICS 260 and 261, or equivalent. Familiarity with Python coding and basic statistics at level of STATS 116. This course runs for the first ten weeks of the quarter.

Schedule for PHYSICS 366
2016-2017 Winter
PHYSICS 366 | 2 units | Class # 32621 | Section 01 | Grading: Letter or Credit/No Credit | LEC
01/09/2017 - 03/17/2017 Tu, Thu 3:00 PM - 4:50 PM at Building 380 Room 381T with Marshall, P. (PI) and Mantz, A.
Instructors: Marshall, P. (PI) and Mantz, A.
Notes: 2-unit, 10-week, 20-session special topics course.
```

## Class Schedule and Location

This is a ten week, 20 lesson, 2-credit course, running from Tuesday January 10 through Thursday March 16, 2017.

Classes will be **Tu,Th 3:00-4:20pm in Building 380 Room 381T.**

Each of the 20 sessions will be 80 minutes long, and will include time to do exercises and go through homework.

[Back to PHYS366 home](https://github.com/KIPAC/StatisticalMethods/blob/master/README.md)

----

## Course Description and Prerequisites

Existing and emerging statistical techniques and their application to
astronomical surveys and cosmological data analysis. Topics covered
will include statistical frameworks (Bayesian inference and
frequentist statistics), numerical methods including Markov Chain
Monte Carlo, and machine learning applied to classification and
regression. Hands on activities based on open-source software in
python.

The course is aimed at graduate students intending to do research in
astrophysics and cosmology.  The level will be aimed at first and
second year students, but more advanced students are welcome.

[PHYSICS 160/260](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CB4QFjAA&url=https%3A%2F%2Fexplorecourses.stanford.edu%2Fsearch%3Fview%3Dcatalog%26filter-coursestatus-Active%3Don%26page%3D0%26catalog%3D%26q%3DPHYSICS%2B260%253A%2BIntroduction%2Bto%2BStellar%2Band%2BGalactic%2BAstrophysics%26collapse%3D&ei=CyeLVYjoOpTtoATIi4aIAw&usg=AFQjCNEOtbEuUK5J_-aRnBLSGTMC-itFTQ&sig2=nrrWmJEjwWbTA7t0oJaksQ) and
[PHYSICS 161/261](https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&page=0&catalog=&academicYear=&q=PHYSICS+261+Introduction+to+Extragalactic+Astrophysics+and+Cosmology&collapse=), or equivalent (ie. advanced undergraduate courses in cosmology and astrophysics) are recommended.  However, we aim to make the course accessible and relevant to first year graduate students intending to work in astrophysics and cosmology, even if they do not have extensive experience in these fields.  

Basic familiarity with Python coding (or willingness to learn quickly!), and basic statistics at the level of [STATS 116](https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&page=0&catalog=&academicYear=&q=STATS+116%3A+Theory+of+Probability&collapse=) (Old notes available [here](http://statweb.stanford.edu/~susan/courses/s116/)) are expected.

Related courses:
[PHYSICS 100](https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&page=0&catalog=&academicYear=&q=PHYSICS+100%3A+%3A+Introduction+to+Observational+and+Laboratory+Astronomy&collapse=) (Introduction to Observational and Laboratory Astronomy) will cover basic practical error analysis, and
[PHYSICS 363]() (Computational Cosmology and Astrophysics) will cover some research making use of techniques introduced in PHYS 366).

[Back to PHYS366 home](https://github.com/KIPAC/StatisticalMethods/blob/master/README.md)

----

## Course Requirements

#### Class Participation:
This is intended to be a hands-on, participatory course, so regular attendance
and active participation is expected. Class participation will contribute 20%
of the final grade.

#### Homework

There will be six homeworks in the 10-week course, due on Tuesdays
before class.  Each homework will contribute 7.5% of the final grade.

Homework assignments will be made available via GitHub.  Instructions can be found below; we will go through these instructions on the first day of class.

#### Final Project
Each student will be required to present a final project.
Projects will be presented during the final class on March 16,
and final written reports will be due on March 30.
The final project will contribute 35% of the final grade.

[Back to PHYS366 home](https://github.com/KIPAC/StatisticalMethods/blob/master/README.md)

----

## Homework

[Familiarity with
GitHub](https://github.com/KIPAC/StatisticalMethods/blob/master/doc/GettingStarted.md#github)
will be rapidly generated early in the course, and then assumed. You'll
need to fork the homework repo, and clone it to your local machine. If
you cannot navigate to [the homework
repository](https://github.com/drphilmarshall/PHYS366-Homework-2017) to
fork it, that's because you have not been given read access to it yet.
<!-- To request
this, please come and introduce yourself to your teachers and classmates
at [the sign-up issue thread](https://github.com/KIPAC/StatisticalMethods/issues/25).-->

#### Getting your Homework Assignments:

Notebooks containing homework assignments will be uploaded to the
[private homework
repository](https://github.com/drphilmarshall/PHYS366-Homework-2017) as
we go. You'll need to fork this repo, and then `git clone` to your
machine so that you can work on them.

Each week, new assignments will appear, in the "base" repository.  To
get them, you will need to be able to pull directly from this repository -
which means that you need to connect to the base repo by adding it as
another "remote."

To tell `git` that you want to connect to the
base repository, do:
```bash
git remote add base git@github.com:drphilmarshall/PHYS366-Homework-2017.git
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

[Back to PHYS366 home](https://github.com/KIPAC/StatisticalMethods/blob/master/README.md)
