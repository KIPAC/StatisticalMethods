# Information for Stanford Students

* [Class Description, Schedule and Location](#whenwhere)
* [Communication](#comm) 
* [Computing](#computing) 
* [Course Requirements](#require)
* [Class Participation](#particip)
* [Homework Guidelines](#hw)
* [Final Project Guidelines](#projects)

## <a name="whenwhere"></a>Class Description, Schedule and Location

See the entry for PHYSICS 366 in [ExploreCourses](https://explorecourses.stanford.edu) for the description, meeting times, and classroom.
A preliminary schedule for the course is found [here](Schedule.md).

#### Students with Documented Disabilities

Students who may need an academic accommodation based on the impact of a disability must initiate the request with the Office of Accessible Education (OAE).  Professional staff will evaluate the request with required documentation, recommend reasonable accommodations, and prepare an Accommodation Letter for faculty dated in the current quarter in which the request is being made. Students should contact the OAE as soon as possible since timely notice is needed to coordinate accommodations.  The OAE is located at 563 Salvatierra Walk (phone: 723-1066, URL: http://oae.stanford.edu).

## <a name="comm"></a>Communication

Outside of class, we will make any important announcements through the "issues" of the [2019 homework GitHub repository](https://github.com/abmantz/phys366_2019) (see below). This means that you must "watch" the HW repo by clicking the Watch (eyeball) button on its main GitHub page. Also, double-check your GitHub notification preferences to make sure that you'll get emails or be otherwise  notified about repositories you're watching. The issues can also be used to ask us questions or raise issues (!) related to the course.

We also have a [Slack](https://physics366.slack.com) team set up for the course, which you can use use to communicate with other students or with the instructors if you wish. Bug one of us if you haven't been invited to join this team by the second week of class.

## <a name="computing"></a>Computing

### Facilities

Likely it will easiest for you to do computing on either your own system or one provided by your lab. If this doesn't work for you, there is a Stanford-wide unix system accessible to all
Stanford students documented [here](https://itservices.stanford.edu/service/sharedcomputing), including a "Getting Started" if you are unfamiliar with unix. Note
that the appropriate cluster to use is `corn` (interactive use,
including compute-intensive tasks). These systems have `git` and
`python` installed, but (as of 2015) appear to have an old version of `notebook`,
so you should follow the instructions above for installing `miniconda`
and the required `python` packages within your home space.

### Use of external codes

One of the strengths of Python as a computing environment is the wealth of freely available code that already exists. In some cases, we will specify that you must write your own code to accomplish a certain task, but otherwise you are free to use existing packages. However, in the case of Markov Chain Monte Carlo sampling, a key algorithmic component of the course, one very important additional rule applies:

1. **You may not use a third-party implementation of an MCMC method unless you can explain how the method works.**



## <a name="require"></a>Course Requirements

1. **Class Participation:**
This is a hands-on, participatory course, in which a significant amount of class time is devoted to collaborative work on exercises and tutorials.
Regular attendance and active participation are both expected and required.
Class participation will contribute 33% of the final grade.

2. **Homework:**
There will be homework assignments approximately weekly.
Homework will contribute a total of 33% of the final grade.

3. **Final Project:**
Each student will be required to present a final project.
Projects will be presented during the final week of class (week of June 3rd),
and final written reports will be due on the last day of the exam period (June 12th).
The final project will contribute 34% of the final grade.

Everyone involved in this course is expected to abide by the [Rules of Engagement](RulesOfEngagement.md) both inside and outside of class, as well as the Stanford Honor Code.

## <a name="particip"></a>Class Participation

Exercises are short problems that are mixed in with the lecture material. These typically involve discussing the solution with a partner, at the level of sketching on paper or on a whiteboard.

Tutorials are more involved problems that require coding, for which a skeleton of code is usually already provided. These are also to be worked on with a partner. Tutorials take place during class, but are separate from the lecture. Typically, there will be one ~40-minute tutorial per week, often serving as an introduction to the week's homework assignment.

Broadly speaking, exercises are for *thinking*, while tutorials are for *doing*.

Note that official solutions will not be provided for the tutorials (or the exercises for that matter), although both will be discussed in class. This reflects the practical nature of the course - **in order to learn the material, you must do the work**.

## <a name="hw"></a>Homework Guidelines

There will be approximately eight homework assignments, released weekly and due one week later.
While there will be no official solutions, we will provide feedback on each submitted assignment, and may point out submissions that provide particularly clear and/or complete solutions (see Mechanics, below).

Homework solutions may be submitted late if there's a good excuse and this is approved ahead of time. Solutions may be improved in response to feedback and re-submitted after the deadline. Credit will generally still be given in both cases, but expectations will be slightly higher than otherwise.

### Collaboration

We encourage students to collaborate on solving the assigned problems, including
* discussing the problems with your classmates,
* working together to solve the problems,
* surveying any other solutions that have been shared in the homework repo.

The idea is that, by working together, we can produce the best possible solution to every homework problem in the course.

This means that a single solution could be submitted by multiple collaborators (see "Mechanics", below), or that one student's solution might make use of another student's work or insight. In the latter case, input from the second student must be explicitly acknowledged. This is how the scientific community works.

In the unlikely event that enrollment greatly exceeds our expectations, we might require homework solutions to be submitted by pairs/groups of students rather than individuals. Otherwise, the extent of your collaboration is up to you.

### Expectations

Your solutions should

1. Be readable. This means there must be enough explanatory prose that we can understand what you're doing in code. Do not assume we can understand the code itself, or rely exclusively on inline comments (though including these is obviously fine and encouraged).

2. Be functional. We should be able to view your solutions (obviously) and run any code in your solution from beginning to end to reproduce your results (modulo noise due to any monte carlo methods used). If you plan to include some non-standard file format (e.g. other than plain text, Jupyter notebook, PDF, JPEG, ...), check with us ahead of time. While you are not strictly required to use Jupyter and Python for code, if you plan to use some other language, you should run this by us also. If some intermediate part of the code takes more than ~1 minute to run, it's fine to comment out the slow line (with an explanation!) and replace it with a one that reads in saved intermediate results.

3. Be complete. This means that results in the form of outputs and plots that are part of your solution should be included (even though we will re-run your code). This sounds obvious, but we mention it because it conflicts with the usual "best practices" for using git repositories.

Each week we will also ask you to provide feedback on the week's homework and tutorial, so that they can be improved in future years. This is required, although the responses will be anonymized.

### Mechanics

Homework will be distributed through this public course repository and collected through a [private GitHub repository](https://github.com/abmantz/phys366_2019) (*separate from this one*) which only Stanford University PHYSICS 366 instructors and students can access.
If you cannot navigate to the link above, that's because you have not been given read access to it yet.
You will need to create a GitHub account for yourself (if you don't already have one) and provide one of the instructors with your user name so that you can be added.
Once you have access, you will need to fork the HW repo, and then clone your fork to your local machine; see [GettingStarted](GettingStarted.md). (Strictly speaking, the forking step is not necessary, but in principle having a fork simplifies the process of collaborating with other students.)

Note that when others fork the repository, GitHub may set you up to be `Watching` those forks, depending on your settings. If you want to avoid getting notifications related to these, go ahead and `Unwatch` them. **Make sure that you are still watching the base HW repo**, however, as we will use it to make announcements.

Each assignment will appear in the [`homework` folder of the public repo](../homework), and will be announced via an issue in the private repository. When this happens, you should immediately copy the assignment notebook to your local clone of the private repository. This is to avoid the possibility of creating conflicts with the public repo, and because you will submit your solution by pull request to the private repo, not the public one.


#### <a name="submission">Submitting your Solutions

In the private repo, within the folder corresponding to a given week's assignment, create a subfolder called by your name (or the names of all students who collaborated directly on your solutions), e.g. `HW_week1/Phil/`, `HW_week2/Adam+Phil/` etc. Keep all materials related to your solutions in that subfolder. This will greatly reduce confusion, and enable us to merge in all your solutions to the base repo for grading.

If you're working in a group, only one copy of the solution needs to be uploaded. Please list the names of your collaborators in some prominent place in the solution itself (see the note on accreditation above!), as well as in the subfolder name.

Use `git add yourfolder`, `git commit` and `git push origin master` to upload the solutions to your remote fork (whose name is "origin"), or to update them after an initial upload. You can then submit a "pull request" from your fork to the base repository on GitHub.
This notifies us that you would like to merge your solutions into the base repository, which we can do after verifying that doing so is safe (e.g. no important files will be overwritten, which should be the case if you've followed these instructions). 

Your solutions themselves obviously need to be in some digital form. If your solutions involve multiple files, you might want to include a `README.md` to explain what each one is and where we should be looking.

## <a name="projects"></a>Final Project Guidelines

Projects will be presented during the final week of class, and final written reports will be due at the end of the exam period (see above).
Students are, as always, encouraged to work in groups.
However, we expect the ambition of the project, and consequently the length of the presentation and write-up, to reflect the number of people working on it.

There are a few [project milestones](ProjectMilestones.md) to be completed and submitted along with (and in the same manner as) the homework assignments. The timeline can be found in our [course schedule](Schedule.md).

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

1. A presentation to be delivered in the final class meeting (or the penultimate class, depending on how many projects there are). This should be pitched at a level understandable to your classmates, and cover the required points above. The time available will depend on the class size, but typically we expect about 10 minutes minimum per project, or about 5 minutes per team member (if there are more than two), with 5 minutes for questions afterwards.

2. The written report will be submitted in the same manner as homework assignments, and should comprehensively cover the points above. The report should be written using LaTeX (a markup language used to produce most physics publications). If you've never used LaTeX before, you will soon enough, so this is as good a time as any to learn; we will provide a template to get you started. Your submission should include your LaTeX source and supporting files (e.g. figures). We'll use the source files to combine everyone's reports into a single document immortalizing your accomplishments. While the report's format is broadly that of a journal article, you should provide adequate detail throughout (as described above) even though this may go beyond what would normally appear in a journal. All members of the group are coauthors of the report, and any substantive contributions from other students (e.g. through discussions) should be acknowledged.

