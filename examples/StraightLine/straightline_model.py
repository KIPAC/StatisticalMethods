def straight_line_log_likelihood(theta, x, y, sigmay):
    """
    Computes the log-likelihood of the straight line model parameters theta given data y

    Parameters
    ----------
    theta : tuple, float
        (m,b) parameter vector: m = slope, b = intercept
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
    "true" values y_t are given by the straight line model

    y_t = m * x + b

    """
    m,b = theta
    return (np.sum(np.log(1./(np.sqrt(2.*np.pi) * sigmay))) +
            np.sum(-0.5 * (y - (m*x + b))**2 / sigmay**2))


def straight_line_log_prior(theta, theta_limits):
    """
    Computes the log-prior PDF for the straight line model parameters theta

    Parameters
    ----------
    theta : tuple, float
        (m,b) parameter vector: m = slope, b = intercept
    theta_limits : tuple of lists, float
        uniform prior bounds on m and b

    Returns
    -------
    scalar log prior PDF

    Notes
    -----
    Prior on both parameters is assumed to be uniform.

    """
    m, b = theta
    mlimits, blimits = theta_limits

    # Uniform in m:
    if (m < mlimits[0]) | (m > mlimits[1]):
        log_m_prior = -np.inf
    else:
        log_m_prior = np.log(1.0/(mlimits[1] - mlimits[0]))
    # Uniform in b:
    if (b < blimits[0]) | (b > blimits[1]):
        log_b_prior = -np.inf
    else:
        log_b_prior = np.log(1.0/(blimits[1] - blimits[0]))

    return log_m_prior + log_b_prior


def straight_line_log_posterior(theta, x, y, sigmay, theta_limits):
    """
    Computes the log of the unnormalized posterior PDF for theta given y.
    """
    return (straight_line_log_likelihood(theta, x, y, sigmay) +
            straight_line_log_prior(theta, theta_limits))
