# numpy: numerical library
import numpy as np
# avoid broken installs by forcing Agg backend...
#import matplotlib
#matplotlib.use('Agg')
# pylab: matplotlib's matlab-like interface
import pylab as plt

# The data we will fit, sometimes:
#  x, y, sigma_y
data1 = np.array([[201,592,61],[244,401,25],[47,583,38],[287,402,15],[203,495,21],
                  [58,173,15],[210,479,27],[202,504,14],[198,510,30],[158,416,16],
                  [165,393,14],[201,442,25],[157,317,52],[131,311,16],[166,400,34],
                  [160,337,31],[186,423,42],[125,334,26],[218,533,16],[146,344,22]]).astype(float)

# plotting limits
xlimits = [0,350]
ylimits = [0,250]
title_prefix = 'Straight line'
plot_format = '.png'

# uniform prior
# mlimits = [1.9, 2.6]
# blimits = [-20, 80]
# mlimits = [-2.0, 2.0]
# blimits = [-200, 200]
# mlo,mhi = mlimits
# blo,bhi = blimits
slimits = [0.001,100]
slo,shi = slimits

def pdf_contour_levels(p):
    sortp = np.sort(p.ravel())
    cump = sortp.cumsum()
    return [sortp[cump > cump.max() * f].min()
            for f in [0.05, 0.32]]

def plot_mcmc_results(chain,mlimits,blimits):
    # Pull m and b arrays out of the Markov chain.
    mm = [m for b,m in chain]
    bb = [b for b,m in chain]
    # Scatterplot of m,b posterior samples
    plt.clf()
    plt.contour(bgrid, mgrid, posterior, pdf_contour_levels(posterior))
    plt.plot(bb, mm, 'b.', alpha=0.1)
    plot_mb_setup(mlimits,blimits)
    plt.show()

    # Histograms
    import corner
    corner.corner(chain, labels=['b','m'], extents=[0.99]*2)
    plt.show()

    # Traces
    plt.clf()
    plt.subplot(2,1,1)
    plt.plot(mm, 'k-')
    plt.ylim(mlimits[0],mlimits[1])
    plt.ylabel('m', fontsize=16)
    plt.subplot(2,1,2)
    plt.plot(bb, 'k-')
    plt.ylabel('b', fontsize=16)
    plt.ylim(blimits[0],blimits[1])
    plt.show()


def plot_mb_setup(mlimits,blimits):
    plt.xlabel('Intercept $b$', fontsize=16)
    plt.ylabel('Slope $m$', fontsize=16)
    plt.axis([blimits[0],blimits[1], mlimits[0],mlimits[1]])

def get_data_no_outliers():
    # pull out the x, y, and sigma_y columns, which have been packed into the
    # "data1" matrix.  "data1" has shape (20,3).  ":" means "everything in
    # that dimension".  Some of the first 5 points are outliers so for this
    # part we only grab from index 5 on, with magic "5:"
    x = data1[5:,0]
    y = data1[5:,1]
    sigmay = data1[5:,2]
    return (x, y, sigmay)

def get_data_with_outliers():
    x = data1[:,0]
    y = data1[:,1]
    sigmay = data1[:,2]
    return x,y,sigmay

def generate_data(seed=None):
    '''
    Generate a data set, with x and sigma_y as standard, but with
    y values given by

    y = a_0 + a_1 * x + a_2 * x**2 + a_3 * x**3 + noise

    '''
    # x = data1[5:,0]
    # sigmay = data1[5:,2]

    Ndata = 30

    xbar = 0.5*(xlimits[0] + xlimits[1])
    xstd = 0.25*(xlimits[1] - xlimits[0])

    if seed is not None:
        np.random.seed(seed=seed)

    x = xbar + xstd * np.random.randn(Ndata)

    meanerr = 0.025*(xlimits[1] - xlimits[0])

    sigmay = meanerr + 0.3 * meanerr * np.abs(np.random.randn(Ndata))

    a = np.array([37.2,0.93,-0.002,0.0])
    y = a[0] + a[1] * x + a[2] * x**2 + a[3] * x**3 + sigmay*np.random.randn(len(x))

    return x,y,sigmay

# Plot data with error bars, standard axis limits, etc.
def plot_yerr(x, y, sigmay):
    # plot data with error bars
    plt.errorbar(x, y, yerr=sigmay, fmt='.', ms=7, lw=1, color='k')
    # if you put '$' in you can make Latex labels
    plt.xlabel('$x$', fontsize=16)
    plt.ylabel('$y$', fontsize=16)
    plt.xlim(*xlimits)
    plt.ylim(*ylimits)
    # plt.title(title_prefix)

# Plot a   y = mx + b  line.
def plot_line(m, b, **kwargs):
    x = np.array(xlimits)
    y = b + m*x
    p = plt.plot(x, y, 'k-', alpha=0.5, **kwargs)
    plt.xlim(*xlimits)
    plt.ylim(*ylimits)
    return p
