# Information for Stanford Students

From the course handbook:
```
PHYSICS 366: Special Topics in Astrophysics: Statistical Methods

Existing and emerging statistical techniques and their application to astronomical surveys and cosmological data analysis. Topics covered will include statistical frameworks (Bayesian inference and frequentist statistics), numerical methods including Markov Chain Monte Carlo, and machine learning applied to classification and regression. Hands on activities based on open-source software in python.

Schedule for PHYSICS 366
2016-2017 Winter
PHYSICS 366 | 2 units | Class # 32621 | Section 01 | Grading: Letter or Credit/No Credit | LEC
01/09/2017 - 03/17/2017 Tu, Thu 3:00 PM - 4:50 PM at Building 380 Room 381T with Marshall, P. (PI) and Mantz, A.
Instructors: Marshall, P. (PI) and Mantz, A.
Notes: 2-unit, 10-week, 20-session special topics course.
```

See below for
* [Class Schedule and Location](#whenwhere)
* [Course Requirements](#require)
* [Communication](#comm)
* [Homework Guidelines](#hw)
* [Final Project Guidelines](#projects)
* [Computing](#computing)

## <a name="whenwhere"></a>Class Schedule and Location

This is a ten week, 20 lesson, 2-credit course, running from Tuesday January 10 through Thursday March 16, 2017.

Classes will be **Tu,Th 3:00-4:20pm in Building 380 Room 381T.**

Each of the 20 sessions will be 80 minutes long, and will include time to do exercises and go through homework.

## <a name="require"></a>Course Requirements

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
and final written reports will be due on March 23.
The final project will contribute 35% of the final grade.

## <a name="comm"></a>Communication

Outside of class, we will make any important announcements through the "issues" of the [2017 homework GitHub repository](https://github.com/drphilmarshall/PHYS366-Homework-2017) (see below). This means that you must "watch" the HW repo by clicking the Watch (eyeball) button on its main GitHub page. Also, double-check your GitHub notification preferences to make sure that you'll get emails or be otherwise  notified about repositories you're watching. The issues can also be used to ask us questions or raise issues (!) related to the course.

We also have a [Slack](http://slack.com) team set up for the course, which you can use use to communicate with other students or with the instructors if you wish. Bug one of us if you haven't been invited to join this team by the second week of class.


## <a name="hw"></a>Homework Guidelines

Each assignment will consist of one relatively short exercise and one more involved problem.
There will be approximately eight homework assignments, released weekly and due one week later.
We will discuss solutions in class on the day that homework is due.

### Presenting Homework Solutions

Each student will be responsible for presenting at least one solution (class size dependent) during the quarter.
The student presenting a given problem will be notified one week in advance, when that assignment is released.

You should approach these presentations as though you were giving a very short talk (probably something like 5-10 minutes) at a conference;
in other words, put a reasonable amount of effort into organizing your solutions and making them presentable.

Like any other class discussion, presenting and discussing homework solutions is part of the "class participation" aspect of the course.
If your presentation requires some file(s) in addition to the solutions themselves (e.g. slides), it should be submitted along with your solutions through the same mechanism (see below).

### Collaboration

We encourage students to collaborate on solving the assigned problems, and even on the presentation material if they wish.

Each presentation is ultimately the responsibility of a single presenting student.
However, you are encouraged to:

* discuss the problem with your classmates,
* work together to solve the problems,
* survey any other solutions that have been shared in the student forks of the homework repo,
* make use of all of this in your presentation.

The idea is that, by working together, we can produce the best possible solution to every homework problem in the course.

Remember that, whenever you make use of any other student's work, _you must acknowledge it, and them, in your presentation_. This is how the scientific community works.

### Mechanics

Homework will be distributed and collected through a [private GitHub repository](https://github.com/drphilmarshall/PHYS366-Homework-2017) (separate from this one) which only PHYSICS 366 instructors and students can access.
If you cannot navigate to the link above, that's because you have not been given read access to it yet.
You will need to create a GitHub account for yourself (if you don't already have one) and provide one of the instructors with your user name so that you can be added.
Once you have access, you will need to fork the HW repo and then clone the fork to your local machine (see [GettingStarted](GettingStarted.md)). Each assignment will appear in the [private base Homework repository](https://github.com/drphilmarshall/PHYS366-Homework-2017), and will be announced via an issue in that repository.

Note that GitHub may set you up to be watching other people's forks of the repo, depending on your settings. If you want to avoid getting notifications related to these, go ahead and unwatch them. **Make sure that you are still watching the base HW repo**, however, as we will use it to make announcements.

#### <a name="gettingassignments">Getting Assignments

When we assign them, homework problems will appear on the base HW repo.
To get them, you will need to be able to pull directly from this repository -
which means that you need to connect to the base repo by adding it as
another "remote."

On your local machine, to tell `git` that you want to connect to the
base repository, do:
```bash
git remote add base git@github.com:drphilmarshall/PHYS366-Homework-2017.git
```
Once you have done this, you should be able to get the latest homework assignment at any time with
```bash
git pull base master
```

#### <a name="submission">Submitting your Solutions

Within the folder corresponding to a given week, create a subfolder called by your GitHub username (or the names of all students who collaborated directly on your solutions), eg `Week1/phil`, `Week2/adam+phil` etc. Keep all materials related to your solutions in that subfolder. This will greatly reduce confusion, and enable us to merge in all your solutions to the base repo for grading.

If you're working in a group, only one copy of the solution needs to be uploaded. Please list the names of your collaborators in some prominent place in the solution itself (see the note on accreditation above!), as well as in the subfolder name.

Use `git add yourfolder`, `git commit` and `git push origin master` to upload the solutions to your remote fork (whose name is "origin"), or to update them after an initial upload.

When you're finished, and your fork is up to date, submit a "pull request" from your fork to the base repository. This notifies us that you would like to merge your solutions into the base repository, which we can do after verifying that doing so is safe (e.g. no important files will be overwritten, which should be the case if you've followed these instructions).

Your solutions themselves obviously need to be in some digital form. The only restriction on format is that they need to be in a form that we can see without installing special software - typically something like PDF, Jupyter notebook or plain text (for code). If your solutions involve multiple files, you might want to include a `README.md` to explain what each one is and where we should be looking.


## <a name="projects"></a>Final Project Guidelines

Projects will be presented during the final class on March 16, and final written reports will be due on March 23 at 6:00 PM. Students are encouraged to work in groups and, unlike homeworks, there will be only one presentation and one report per group. However, we expect the ambition of the project, and consequently the length of the presentation and write-up, to reflect the number of people working on it.

The timeline for projects is

* First ~half of the course: brainstorm ideas
* Week 6 *at the latest*: arrange to pitch your idea to Phil and/or Adam. We'll give you feedback as to whether the content and scope are appropriate. The homework due this week will include writing a brief abstract describing your project.
* Weeks 6-10: work on the project with your teammates.
* March 16: presentations
* By March 23: turn in written report by 6PM

The purpose of these projects is to apply what you've learned in the course (or go beyond it) to a real or realistic data analysis problem. The problem may be from your own research, although it need not be.

You do not have to limit yourselves to projects that can be fully completed in just a few weeks. Especially if the project is relevant to your research, it's fine to pitch a more ambitious project and not reach the end of it during the course. However, it should be possible to present some progress and understanding after a few weeks, even if the inferences are limited to simulated data and/or a simplified version of the full problem.

### Requirements

We anticipate significant variety in the projects people pursue, but the following elements are broadly required in the presentations and reports.

* A brief introduction to the data being analyzed.
* A discussion of the model you are investigating, including a cartoon
showing its parameters, and a list of the assumptions you make (in some form).
* A probabilistic graphical model, accompanied by the probability expressions that go with it.
* A description of any approximations you make in deviating from the
probability theory you outline.
* Visualisations of your inferences, including verification of convergence etc.
* Discussion of how you would, given more time, extend this analysis -
including conclusions of what worked well, and what did not.

### Deliverables

1. A presentation to be delivered in the final class meeting. This should be pitched at a level understandable to your classmates, and cover the required points above. The time available will depend on the class size, but typically we expect about 10 minutes minimum per project, or about 5 minutes per team member (if there are more than two), with 5 minutes for questions afterwards.

2. The written report will be submitted in the same manner as homework assignments, and should comprehensively cover the points above. The report should be written using LaTeX (a markup language used to produce most physics publications). If you've never used LaTeX before, you will soon enough, so this is as good a time as any to learn; we will provide a template to get you started. Your submission should include your LaTeX source and supporting files (e.g. figures). We'll use the source files to combine everyone's reports into a single document immortalizing your accomplishments.

## <a name="computing"></a>Computing

Likely it will easiest for you to do computing on either your own system or one provided by your lab. If this doesn't work for you, there is a Stanford-wide unix system accessible to all
Stanford students documented [here](https://itservices.stanford.edu/service/sharedcomputing), including a "Getting Started" if you are unfamiliar with unix. Note
that the appropriate cluster to use is `corn` (interactive use,
including compute-intensive tasks). These systems have `git` and
`python` installed, but (as of 2015) appear to have an old version of `notebook`,
so you should follow the instructions above for installing `miniconda`
and the required `python` packages within your home space.
