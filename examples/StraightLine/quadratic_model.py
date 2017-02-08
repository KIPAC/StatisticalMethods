def quadratic_log_likelihood(theta, x, y, sigmay):
    """
    Computes the log-likelihood of the quadratic model parameters theta given data y

    Parameters
    ----------
    theta : tuple, float
        (m,b,q) parameter vector: m = slope, b = intercept, q = quadratic term coefficient
    x : ndarray, float
        x coordinates
    y : ndarray, float
        "observed" y values
    sigmay : ndarray, float
        observational uncertainties on y

    Returns
    -------
    scalar log likelihood

    Notes
    -----
    Data y exist at given values of x, and are assumed to have Gaussian
    measurement noise with known standard deviation sigmay, where the
    "true" values *y_t* are given by the straight line model

    y_t = m * x + b + q*x**2

    """
    m, b, q = theta
    return (np.sum(np.log(1./(np.sqrt(2.*np.pi) * sigmay))) +
            np.sum(-0.5 * (y - (m*x + b + q*x**2))**2 / sigmay**2))


def quadratic_log_prior(theta, theta_limits):
    """
    Computes the log-prior PDF for the quadratic model parameters theta

    Parameters
    ----------
    theta : tuple, float
        (m,b,q) parameter vector: m = slope, b = intercept, q = quadratic term coefficient
    theta_limits : tuple of lists, float
        uniform prior bounds on m and b, Gaussian mean and width for q

    Returns
    -------
    scalar log prior PDF

    Notes
    -----
    Prior on m and b parameters is assumed to be uniform, while
    prior on q is assumed to be a not unreasonable Gaussian.

    """
    m, b, q = theta
    mlimits, blimits, qpars = theta_limits

    # m and b:
    log_mb_prior = straight_line_log_prior(np.array([m,b]), np.array([mlimits, blimits]))
    # q:
    log_q_prior = np.log(1./(np.sqrt(2.*np.pi) * qpars[1])) - \
                  0.5 * (q - qpars[0])**2 / qpars[1]**2
    return log_mb_prior + log_q_prior


def quadratic_log_posterior(theta, x, y, sigmay, theta_limits):
    """
    Computes the log of the unnormalized posterior PDF for theta given y.
    """
    return (quadratic_log_likelihood(theta, x, y, sigmay) +
            quadratic_log_prior(theta, theta_limits))
