import numpy as np

def plot_traces(samples, axes, labels=None, truths=None,
                    Line2D_kwargs={},
                    truth_kwargs={}):
    '''
    Plot traces of parameters in a Markov chain.

    `samples` can be a 2D array with each parameter having its own column,
      a list thereof, or a 3D array with the first index giving chain number.
    `axes` should be a list of thingies to plot into
    `labels`: optional name for each parameter
    `truths`: optional value to plot as a horizontal line in each pane
    `Line2D_kwarg`, `truth_kwargs`: dictionaries of options to pass to
      Line2D (for the traces) and axhline (for the truth values)

    Example:
      import matplotlib.pyplot as plt
      plt.rcParams['figure.figsize'] = (16.0, 12.0)
      fig, ax = plt.subplots(samples.shape[1], 1);
      plot_traces(samples, ax, ...
    '''
    if samples.__class__ == list:
        chains = samples
    elif len(samples.shape) == 2:
        chains = [samples]
    elif len(samples.shape) == 3:
        chains = [samples[i,:,:] for i in range(samples.shape[0])]    
    else:
        raise Exception('`samples` must be a list or 2D/3D ndarray')
    ax = axes
    try:
        iter(ax)
    except TypeError:
        ax = [axes]
    lkw = {'marker':'.', 'linestyle':''}
    for k in Line2D_kwargs.keys():
        lkw[k] = Line2D_kwargs[k]
    addcolor_trace = ("color" not in lkw.keys())
    addcolor_truth = ("color" not in truth_kwargs.keys())
    for j in range(chains[0].shape[1]):
        for i,s in enumerate(chains):
            if addcolor_trace:
                lkw['color'] = 'C'+str(i)
            ax[j].plot(s[:,j], **lkw);
        if truths is not None:
            if addcolor_truth:
                truth_kwargs['color'] = 'C'+str(i+1)
            ax[j].axhline(y=truths[j], **truth_kwargs);
        if labels is not None:
            ax[j].set_ylabel(labels[j]);


def GelmanRubinR(chains, return_all=False):
    '''
    Computes the Gelman-Rubin convergence criterion for each parameter in `chains`.
    `chains` is a list of numpy arrays, in which each column represents a parameter, and each row an MCMC step,
     OR a 3D numpy array with the 1st index over chains and the second-third as above.
    '''
    if chains.__class__ == list:
        M = len(chains) # number of chains
        N = np.mean([chain.shape[0] for chain in chains]) # number of steps - hopefully all the same or very similar
        # P = number of parameters
        thetaJ = np.array([np.mean(chain, axis=0) for chain in chains]) # shape (M,P)
        s2J = np.array([np.var(chain, axis=0) for chain in chains]) # shape (M,P)
    else:
        M = chains.shape[0]   # number of chains
        N = chains.shape[1]   # number of steps
        # P = number of parameters
        thetaJ = np.mean(chains, axis=1) # shape (M,P)
        s2J = np.var(chains, axis=1) # shape (M,P)
    B = N * np.var(thetaJ, axis=0) # shape (P)
    W = np.mean(s2J, axis=0) # shape (P)
    V = (N-1.0)/N*W + B/N # shape (P)
    R = np.sqrt(V/W) # shape (P)
    if return_all:
        return (R,B,W,V)
    else:
        return R

def effective_samples(chains, maxlag=None, V=None):
    '''
    Computes the effective number of samples for each parameter in `chains`.
    `chains` is a list of numpy arrays, in which each column represents a parameter, and each row an MCMC step.
    
    Pass a guess at the maximum lag we might need to do the calculation for to avoid wasting tons of time.
    Pass in the value of V from GelmanRubinR, or it will be computed internally.
    '''
    def lagfun(x, t):
        # x is an n*m array representing one chain
        n = x.shape[0]
        return np.sum(( x[t:n,:] - x[0:(n-t),:] )**2, axis=0) / (n-t)
    def Vt(chains, t):
        return np.mean([lagfun(chain, t) for chain in chains], axis=0)
    # Vt, V, rhot, neff are all Nparamters length vectors
    if V is None:
        _,_,_,V = GelmanRubinR(chains, return_all=True)
    m = len(chains)
    n = np.mean([chain.shape[0] for chain in chains])
    if maxlag is None:
        maxlag = np.min([chain.shape[0] for chain in chains])
    p = chains[0].shape[1]
    rhot = np.array([1.0-0.5*Vt(chains, t)/V for t in range(1,maxlag+1)])
    neff = np.zeros(p)
    sumof2 = rhot[0:(maxlag-1),:] + rhot[1:maxlag,:]
    warn = False
    for i in range(p):
        j = np.where(sumof2[:,i] < 0.0)[0]
        if len(j) == 0:
            warn = True
            neff[i] = m*n / (1.0 + 2.0*np.sum(rhot[:,i]))
        else:
            neff[i] = m*n / (1.0 + 2.0*np.sum(rhot[0:j[0],i]))
    if warn:
        print("Warning: effective_samples - set maglax higher if possible")
    return neff
