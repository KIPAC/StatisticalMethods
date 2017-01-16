from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

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
        return

    def list_hosts(self):
        # The list of (9) unique galaxy host names:
        return np.unique(self.hosts)

    def select(self, ID):
        # Pull out one galaxy's data from the master array:
        index = (self.hosts == str(ID))
        self.mobs = self.data[index, 2]
        self.merr = self.data[index, 3]
        self.logP = np.log10(self.data[index, 4])
        return

    def plot(self, X):
        # Plot all the points in the dataset for host galaxy X.
        ID = str(X)
        self.select(ID)
        plt.rcParams['figure.figsize'] = (15.0, 8.0)
        plt.rc('xtick', labelsize=16)
        plt.rc('ytick', labelsize=16)
        plt.errorbar(self.logP, self.mobs, yerr=self.merr, fmt='.', ms=7, lw=1, color=self.colors[ID], label='NGC'+ID)
        plt.xlabel('$\\log_{10} P / {\\rm days}$', fontsize=20)
        plt.ylabel('${\\rm magnitude (AB)}$', fontsize=20)
        plt.xlim(self.xlimits)
        plt.ylim(self.ylimits)
        plt.title('Cepheid Period-Luminosity (Riess et al 2011)', fontsize=20)
        return

    def overlay_straight_line_with(self, a=0.0, b=24.0):
        # Overlay a straight line with gradient a and intercept b.
        x = self.xlimits
        y = a*x + b
        plt.plot(x, y, 'k-', alpha=0.5, lw=2)
        plt.xlim(self.xlimits)
        plt.ylim(self.ylimits)
        return

    def add_legend(self):
        plt.legend(loc='upper left')
        return
