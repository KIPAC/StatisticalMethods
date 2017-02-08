def metropolis(log_posterior, theta, theta_limits, stepsize, nsteps=10000):
    """
    Draws samples from a given PDF using the Metropolis Hastings algorithm.

    Parameters
    ----------
    log_posterior : function
        log PDF for parameters theta
    theta : ndarray
        vector of parameters, providing initial position in parameter space
    theta_limits : tuple of lists, float
        set of pairs of parameter limits: uniform prior ranges, or Gaussian mean and width
    stepsize : float, or ndarray
        scalar or vector proposal distribution width
    nsteps : int
        desired number of samples

    Returns
    -------
    chain : 2D ndarray, float
        ensemble of samples, an array of numpy arrays, each one a vector like theta
    log_probs : 1D ndarray
        values of log posterior at each sample
    acceptance_rate : float
        fraction of steps resulting in a successful move
    """

    # Start at theta. Note that the data (x, y, sigmay) are assumed to be globally available
    log_prob = log_posterior(theta, x, y, sigmay, theta_limits)

    # Store Markov chain as an array of samples:
    chain = np.empty((nsteps, len(theta)))
    log_probs = np.empty(nsteps)

    # Count our accepted proposals:
    naccept = 0

    for i in range(nsteps):

        theta_new = theta + stepsize * np.random.randn(len(theta))
        log_prob_new = log_posterior(theta_new, x, y, sigmay, theta_limits)

        if np.log(np.random.rand()) < (log_prob_new - log_prob):
            # accept, and move to the proposed position:
            theta = theta_new
            log_prob = log_prob_new
            naccept += 1

        else:
            # reject, and store the same sample as before:
            pass

        chain[i] = theta
        log_probs[i] = log_prob

    acceptance_rate = naccept/float(nsteps)

    return chain,log_probs,acceptance_rate
