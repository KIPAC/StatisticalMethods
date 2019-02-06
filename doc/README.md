# About this course

Stanford PHYSICS 366 students should see the [Stanford.md](Stanford.md) document in addition to the information below.

Everyone should see the [Getting Started](GettingStarted.md) document to set up their computing environment.

* [Course Description](#descrip)
* [Prerequisites](#prereq)
* [Textbooks](#books)
* [Organization](#org)

## <a name="descrip"></a>Course Description

Foundations of principled inference from data, primarily in the Bayesian framework, organized around applications in astrophysics and cosmology.
Topics include
probabilistic modeling of data,
parameter constraints and model comparison,
numerical methods including Markov Chain Monte Carlo,
and
connections to frequentist and machine learning frameworks.
Hands-on experience with real data through in-class tutorials, problem sets and a final project.

The course is aimed at graduate students intending to do research in astrophysics and cosmology, although the content is broadly applicable to statistical data analysis.

## <a name="prereq"></a>Prerequisites

The following background is recommended.

1. Prerequisite: programming in Python or a similar language (at the level of [CS 106A](https://explorecourses.stanford.edu)).
The first few lessons do not require programming, but this is ultimately a hands-on course in data analysis.
In principle, one could use a different programming language, but since code provided in the tutorials is in Python, we recommend sticking with it for simplicity.

2. Recommended but not required: probability at the level of [STATS 116 or PHYSICS 166/266](https://explorecourses.stanford.edu).
Exposure to probability through other physics courses (statistical or quantum mechanics) may be sufficient, since we will review the subject *briefly* early in the course.

## <a name="books"></a>Textbooks

This course is mostly self-contained, but at the beginning of each lesson we list some opportunities for additional reading.
The most widely useful reference for this course is
* **[Gelman et al., "Bayesian Data Analysis"](http://www.stat.columbia.edu/~gelman/book/)** (3rd ed.) 

Some additional sources are:
* **[MacKay, "Information Theory, Inference and Learning Algorithms"](http://www.inference.phy.cam.ac.uk/mackay/itprnn/book.html)** (free download)
* **[Ivezic et al, "Statistics, Data Mining and Machine Learning in Astronomy"](http://www.astroml.org/)**
* **Ross, "A First Course in Probability"** (7th ed.)
* **Fishman, "A First Course in Monte Carlo"**
* **[Bishop, "Pattern Recognition and Machine Learning,"](https://www.amazon.com/Pattern-Recognition-Learning-Information-Statistics/dp/0387310738)**


## <a name="org"></a>Content

This course is divided into lessons, tutorials and problem sets, each of which resides in a Jupyter Notebook (`.ipynb`) file.
These notebooks can be browsed directly through a web browser (using GitHub's rendering engine) or interacted with on the user's own machine through Jupyter Notebook (see [Getting Started](GettingStarted.md)).
The quickest way to find a particular notebook is probably through the [schedule](Schedule.md).

* **Lessons** are a combination of lecture material, worked examples, demos and exercises, that we will cover in class.
These very rarely involve writing or running code.

* **Tutorials** are involved, *partially* worked problems that do require coding.
The intention is for students to work together to solve these problems *in class*, where immediate feedback from the instructors is possible.

* **Problem sets** are similarly involved problems, generally provided with less guidance, to be completed outside of class.

Note that tutorials and problem sets will only appear here when they are set.

See [Stanford.md](Stanford.md) for policies regarding tutorials, problem sets, and class participation generally in this course.

### Technicalities of Tutorials

As noted above, tutorial notebooks contain some working code, and some that you will need to complete. In practice, that means you will see cells like these in the tutorial notebooks:

```python
try:
	exec(open(Solution/assign_x.py).read())
except IOError:
	x = REPLACE_WITH_YOUR_SOLUTION()
```

Intuitively, the idea is that you should replace `REPLACE_WITH_YOUR_SOLUTION()` with your own code; you can also delete the `try`-`except` construction if it annoys you. *You do **not** need to put your solution to each such code block in a separate file in a `Solution` folder.*

There is a reason for this slightly inconvenient construction! Namely,
1. It allows us to verify that the completed notebook will actually work without having to make any changes to the notebook itself before distributing it (possibly of introducing errors in the process).
2. The code is syntactically correct even though it is incomplete. Attempting to run it as-is will result in an `Exception` pointing out that the solution is incomplete rather than one that might be the result of an actual code error.
