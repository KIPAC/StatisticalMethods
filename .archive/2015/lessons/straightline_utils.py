#Credit Dustin Lang & Phil Marshall
#Source: https://github.com/dstndstn/LearningInference/blob/master/straightline_utils.py
# numpy: numerical library
import numpy as np
import pylab as plt

# The data we will fit:
#  x, y, sigma_y
data1 = np.array([[201,592,61],[244,401,25],[47,583,38],[287,402,15],[203,495,21],
                  [58,173,15],[210,479,27],[202,504,14],[198,510,30],[158,416,16],
                  [165,393,14],[201,442,25],[157,317,52],[131,311,16],[166,400,34],
                  [160,337,31],[186,423,42],[125,334,26],[218,533,16],[146,344,22]]).astype(float)

# plotting limits
xlimits = [0,250]
ylimits = [100,600]
title_prefix = 'Straight line?'
plot_format = '.png'

mlimits = [1.9, 2.6]
blimits = [-20, 80]
mlo,mhi = mlimits
blo,bhi = blimits
slo,shi = [0.001,100]

def pdf_contour_levels(p):
    sortp = np.sort(p.ravel())
    cump = sortp.cumsum()
    return [sortp[cump > cump.max() * f].min()
            for f in [0.32, 0.05]]

def plot_mcmc_results(chain):
    # Pull m and b arrays out of the Markov chain.
    mm = [m for b,m in chain]
    bb = [b for b,m in chain]
    # Scatterplot of m,b posterior samples
    plt.clf()
    plt.contour(bgrid, mgrid, posterior, pdf_contour_levels(posterior))
    plt.plot(bb, mm, 'b.', alpha=0.1)
    plot_mb_setup()
    plt.show()
    
    # Histograms
    import triangle
    triangle.corner(chain, labels=['b','m'], extents=[0.99]*2)
    plt.show()
    
    # Traces
    plt.clf()
    plt.subplot(2,1,1)
    plt.plot(mm, 'k-')
    plt.ylim(mlo,mhi)
    plt.ylabel('m')
    plt.subplot(2,1,2)
    plt.plot(bb, 'k-')
    plt.ylabel('b')
    plt.ylim(blo,bhi)
    plt.show()


def plot_mb_setup():
    plt.xlabel('intercept b')
    plt.ylabel('slope m')
    plt.axis([blo,bhi, mlo,mhi])

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

# Plot data with error bars, standard axis limits, etc.
def plot_yerr(x, y, sigmay):
    # plot data with error bars
    plt.errorbar(x, y, yerr=sigmay, fmt='.', ms=7, lw=1, color='k')
    # if you put '$' in you can make Latex labels
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.xlim(*xlimits)
    plt.ylim(*ylimits)
    plt.title(title_prefix)

# Plot a   y = mx + b  line.
def plot_line(m, b, **kwargs):
    x = np.array(xlimits)
    y = b + m*x
    p = plt.plot(x, y, 'k-', alpha=0.5, **kwargs)
    plt.xlim(*xlimits)
    plt.ylim(*ylimits)
    return p
