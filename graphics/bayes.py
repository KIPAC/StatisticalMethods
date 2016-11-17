import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rcParams['xtick.labelsize'] = 'x-large'
plt.rcParams['ytick.labelsize'] = 'x-large'
import numpy as np
from scipy.special import gamma as Gamma
import scipy.stats as st

# scipy.stat's implementation of the Gamma distribution is ridiculous
def GammaPDF(x,a,b):
    return b**a * x**(a-1.0) * np.exp(-b*x) / Gamma(a)

def bayesDemo(alpha0, beta0, N, showLikelihood=False):
    mu = np.linspace(0.0, np.max([10.0, N+5.0*np.sqrt(N)]), 100)
    prior = GammaPDF(mu, alpha0, beta0)
    like = st.poisson.pmf(N,mu)
    post = GammaPDF(mu, alpha0+N, beta0+1)
    postLine, = plt.plot(mu,post)
    priorLine, = plt.plot(mu,prior)
    if showLikelihood:
        likeLine, = plt.plot(mu,like)
        plt.legend((priorLine, likeLine, postLine), ('Prior', 'Likelihood', 'Posterior'))
    else:
        dataLine, = plt.plot([N]*2, [0.0, np.max(post)*1.1], '--')
        plt.legend((priorLine, dataLine, postLine), ('Prior', 'Measurement', 'Posterior'), fontsize='x-large')
    plt.xlabel(r'$\mu$', fontsize=22)
    plt.ylabel('density', fontsize=22)

