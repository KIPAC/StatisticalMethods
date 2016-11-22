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

## Course Requirements

1. **Class Participation:**
This is intended to be a hands-on, participatory course, so regular attendance
and active participation is expected. Class participation will contribute 20%
of the final grade.

2. **Homework:**
There will be homework assignments approximately weekly.
Homework will contribute a total of 45% of the final grade.

3. **Final Project:**
Each student will be required to present a final project.
Projects will be presented during the final class on March 16,
and final written reports will be due on March 30.
The final project will contribute 35% of the final grade.

----

## Homework

Each assignment will consist of one relatively short exercise and one more involved problem.
We discuss solutions in class on the day that homeworks are due.

Each student will be responsible for presenting at least one solution (class size dependent) during the quarter.
The student presenting a given problem will be determined no later than the actual assignment of the problem, i.e. a week in advance.
You should approach these presentations as though you were giving a very short talk (probably something like 5-10 minutes) at a conference; in other words, put a reasonable amount of effort into organizing your solutions and making them presentable. Like any other class discussion, presenting and discussing homework solutions is part of the "class participation" aspect of the course.

We encourage students to collaborate on solving the assigned problems, and even on the presentation material if they wish. A given actual presentation is, however, ultimately the responsibility of one student.

### Mechanics

Homeworks will be distributed and collected through a [private GitHub repository]((https://github.com/drphilmarshall/PHYS366-Homework-2017)) (separate from this one) which only PHYSICS 366 instructors and students can access.
If you cannot navigate to the link above, that's because you have not been given read access to it yet. You will need to create a GitHub account for yourself (if you don't already have one) and provide one of the instructors with your user name so that you can be added. Once you have access, you will need to fork the HW repo and then clone the fork to your local machine (see [GettingStarted](doc/GettingStarted.md)).

#### Getting assignments

When we assign them, homework problems will appear on the base HW repo.
To get them, you will need to be able to pull directly from this repository -
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

#### Submitting your solutions

Within the folder corresponding to a given problem, create a subfolder called by your name or the names of all students who collaborated on your solutions. Keep all materials related to your solutions in that subfolder. This will greatly reduce confusion.

If you're working in a group, only one copy of the solution needs to be uploaded. Please list the names of your collaborators in some prominent place in the solution itself, in addition to the subfolder name.

Use `git add yourfolder`, `git commit` and `git push origin master` to upload the solutions to your remote fork (whose name is "origin"), or to update them after an initial upload.

When you're finished, and your fork is up to date, submit a "pull request" from your fork to the base repository. This notifies us that you would like to merge your solutions into the base repository, which we can do after verifying that doing so is safe (e.g. no important files will be overwritten, which should be the case if you've followed these instructions).

## Final project
