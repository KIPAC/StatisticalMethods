import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rcParams['xtick.labelsize'] = 'x-large'
plt.rcParams['ytick.labelsize'] = 'x-large'
import numpy as np

def inv_trans_demo(x, lam):
    hist = plt.hist(x, bins=50, normed=True)
    xs = np.linspace(0.0, 10.0/lam, 100)
    pdf = lam * np.exp(-lam*xs)
    pdfline = plt.plot(xs, pdf, 'r', lw=2)
    plt.xlabel(r'x', fontsize=22)
    plt.ylabel(r'P(x)', fontsize=22);
