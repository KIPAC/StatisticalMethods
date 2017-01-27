# About this course

Stanford PHYSICS 366 students should see the [Stanford.md](Stanford.md) document in addition to the information below.

Everyone should see the [Getting Started](GettingStarted.md) document to set up their computing environment.

* [Course Description](#descrip)
* [Prerequisites](#prereq)
* [Textbooks](#books)
* [Organization](#org)

## <a name="descrip"></a>Course Description

Existing and emerging statistical techniques and their application to astronomical surveys and cosmological data analysis. Topics covered will include statistical frameworks (Bayesian inference and frequentist statistics), numerical methods including Markov Chain Monte Carlo, and machine learning applied to classification and regression. Hands on activities based on open-source software in python.

The course is aimed at graduate students intending to do research in astrophysics and cosmology, although the content is broadly applicable to statistical data analysis.

## <a name="prereq"></a>Prerequisites

The following background is recommended.

1. Basic statistics and probability will be reviewed briefly at the beginning of this course.
Previous exposure to these subjects at the undergraduate level in statistics (e.g. [STATS 116](https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&page=0&catalog=&academicYear=&q=STATS+116%3A+Theory+of+Probability&collapse=),
old notes available [here](http://statweb.stanford.edu/~susan/courses/s116/)) or physics
(undergraduate statistical mechanics and/or quantum mechanics) courses will be helpful.

2. Basic familiarity with writing code in Python, or a burning desire to learn quickly. No Python knowledge is needed for the first few lessons, but, this being a hands-on course, the amount of code and coding increases quickly after that. It's of course possible to do the various exercises using some other language or environment; we will stick with Python for consistency.

## <a name="books"></a>Textbooks

This course will be mostly self-contained, but at the beginning of each chunk we list some opportunities for additional reading.
These are mostly drawn from the following sources:
* **[MacKay, "Information Theory, Inference and Learning Algorithms"](http://www.inference.phy.cam.ac.uk/mackay/itprnn/book.html)** (free download)
* **[Ivezic et al, "Statistics, Data Mining and Machine Learning in Astronomy"](http://www.astroml.org/)**
* **[Gelman et al, "Bayesian Data Analysis"](http://www.stat.columbia.edu/~gelman/book/)** (2nd ed.)
* **Ross, "A First Course in Probability"** (7th ed.)
* **Fishman, "A First Course in Monte Carlo"**
* **[Bishop, "Pattern Recognition and Machine Learning,"](https://www.amazon.com/Pattern-Recognition-Learning-Information-Statistics/dp/0387310738)"**

## <a name="org"></a>Organization

The content of this course is divided thematically into "chunks of stuff", each of which resides in a Jupyter Notebook (`.ipynb`) file in the `chunks` folder of this repository.
These notebooks serve dual purposes

1. In class, we use the RISE extension for Jupyter to display them as slides.
2. Each notebook can also be read through directly through a web browser (using GitHub's rendering engine) or interacted with on the user's own machine through Jupyter Notebook.
See [Getting Started](GettingStarted.md).

Each chunk is a combination of lecture material, worked examples, demos (using Python) and exercises.
Their length varies; we expect individual chunks to take between 20 and (at most) 80 minutes of class time.
Bonus exercises (that we typically don't expect to get to during class) often appear at the end of a notebook.
There is a logical order to the chunks, reflected in the [Schedule](../chunks/README.md) document.
