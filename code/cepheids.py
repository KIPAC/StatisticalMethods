from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Data ingest and visualization class
# ----------------------------------------------------------------------

class Cepheids(object):
    """
    Methods for reading in and visualizing the R11 cepheids dataset.
    """
    def __init__(self, filename):
        # Read in the data and store it in this master array:
        self.data = np.loadtxt(filename)
        self.hosts = self.data[:,1].astype('int').astype('str')
        # We'll need the plotting setup to be the same each time we make a plot:
        colornames = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet', 'magenta', 'gray']
        self.colors = dict(zip(self.list_hosts(), colornames))
        self.xlimits = np.array([0.3, 2.3])
        self.ylimits = np.array([30.0, 17.0])
        self.redshifts = {}
        self.redshifts['1309'] = 0.007125
        self.redshifts['3021'] = 0.005140
        self.redshifts['3370'] = 0.004266
        self.redshifts['3982'] = 0.003699
        self.redshifts['4038'] = 0.005477
        self.redshifts['4258'] = 0.001494
        self.redshifts['4536'] = 0.006031
        self.redshifts['4639'] = 0.003395
        self.redshifts['5584'] = 0.005464
        return

    def list_hosts(self):
        # The list of (9) unique galaxy host names:
        return np.unique(self.hosts)

    def select(self, ID):
        # Pull out one galaxy's data from the master array:
        index = (self.hosts == str(ID))
        self.mobs = self.data[index, 2]
        self.sigma = self.data[index, 3]
        self.logP = np.log10(self.data[index, 4])
        return

    def plot(self, X):
        # Plot all the points in the dataset for host galaxy X.
        ID = str(X)
        self.select(ID)
        plt.rcParams['figure.figsize'] = (15.0, 8.0)
        plt.rc('xtick', labelsize=16)
        plt.rc('ytick', labelsize=16)
        plt.errorbar(self.logP, self.mobs, yerr=self.sigma, fmt='.', ms=7, lw=1, color=self.colors[ID], label='NGC'+ID)
        plt.xlabel('$\\log_{10} P / {\\rm days}$', fontsize=20)
        plt.ylabel('${\\rm magnitude (AB)}$', fontsize=20)
        plt.xlim(self.xlimits)
        plt.ylim(self.ylimits)
        plt.title('Cepheid Period-Luminosity (Riess et al 2011)', fontsize=20)
        return

    def overlay_straight_line_with(self, a=0.0, b=24.0, label=None):
        # Overlay a straight line with gradient a and intercept b.
        x = self.xlimits
        y = a*x + b
        plt.plot(x, y, 'k-', alpha=0.5, lw=2, label=label)
        plt.xlim(self.xlimits)
        plt.ylim(self.ylimits)
        return

    def add_legend(self):
        plt.legend(loc='upper left')
        return

    def save_png(self):
        plt.savefig('cepheid_data.png', dpi=300)
        return

    def sufficient_statistics(self):
        x = self.logP
        y = self.mobs
        sigma = self.sigma
        w = 1.0 / sigma**2
        So = np.sum(w)
        Sx = np.sum(w * x)
        Sy = np.sum(w * y)
        Sxy = np.sum(w * x * y)
        Sxx = np.sum(w * x * x)
        Matrix = np.array([[Sxx, Sx], [Sx, So]])
        vector = np.array([Sxy, Sy])
        return Matrix, vector

    def negative_log_likelihood(self, theta):
        """
        Computes -log L(theta)

        Parameters
        ----------
        theta : float, ndarray
            parameters being fitted, (a,b)

        Returns
        -------
        0.5 * chisq
        """
        a, b = theta[0], theta[1]
        chisq = np.sum(((self.mobs - a * self.logP - b) / self.sigma)**2)
        return 0.5 * chisq

# ----------------------------------------------------------------------
# Data analysis functions
# ----------------------------------------------------------------------

def plot_1d_marginalized_pdfs(a, b, Pa, Pb):
    """
    Plot both 1D marginalized posterior distributions for the straight
    line modeling of a Cepheid dataset

    Parameters
    ----------
    a : float, ndarray
        slope parameter array
    b : float, ndarray
        intercept parameter array
    Pa : float, ndarray
        P(slope) PDF array
    Pb : float, ndarray
        P(intercept) PDF array
    """
    fig, (left, right) = plt.subplots(nrows=1, ncols=2)
    fig.set_size_inches(15, 6)
    plt.subplots_adjust(wspace=0.2)

    left.plot(a, prob_a_given_data)
    left.set_title('${\\rm Pr}(a|d)$', fontsize=20)
    left.set_xlabel('slope $a$', fontsize=20)
    left.set_ylabel('Posterior probability density', fontsize=20)

    right.plot(b, prob_b_given_data)
    right.set_title('${\\rm Pr}(b|d)$', fontsize=20)
    right.set_xlabel('intercept $b$ / AB magnitudes', fontsize=20)
    right.set_ylabel('Posterior probability density', fontsize=20)

    return


def compress_1D_pdf(x, pr ,ci=68.3, dp=1):
    """
    Compress a 1D PDF into a median and 68% credible interval

    Parameters
    ----------
    x : float, ndarray
        parameter array
    pr : float, ndarray
        pdf array
    ci : float
        credible interval width
    dp : int
        number of decimal places to report to

    Returns
    report : string
        latex formatted parameter statement
    """
    # Interpret credible interval request:
    low  = (1.0 - ci/100.0)/2.0    # 0.16 for ci=68
    high = 1.0 - low               # 0.84 for ci=68

    # Find cumulative distribution and compute percentiles:
    cumulant = pr.cumsum()
    pctlow = x[cumulant>low].min()
    median = x[cumulant>0.50].min()
    pcthigh = x[cumulant>high].min()

    # Convert to error bars, and format a string:
    errplus = np.abs(pcthigh - median)
    errminus = np.abs(median - pctlow)

    report = "$ "+str(round(median,dp))+"^{+"+str(round(errplus,dp))+"}_{-"+str(round(errminus,dp))+"} $"

    return report
