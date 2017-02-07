def assess_goodness_of_fit(chisq_min, Ndof):
    """
    Parameters
    ----------
    chisq_min : float
        Value of chisq following minimization
    Ndof : int
        No. of degrees of freedom (Ndata - Npars)

    Returns
    -------
    rchisq : float
        Reduced chi-squared value
    p : float
        p-value
    nsigma : float
        No. of sigma we are from an acceptable fit, using Fisher approximation
    """
    import scipy.stats, numpy as np

    # Reduced chi-squared:
    rchisq = chisq_min / (1.0*Ndof)
    # p-value:
    chisq = scipy.stats.chi2(Ndof)
    p = chisq.sf(chisq_min)
    # Nsigma from an acceptable fit:
    nsigma = np.sqrt(2.0*chisq_min) - np.sqrt(2.0*Ndof - 1.0)

    return rchisq, p, nsigma

# Populate table:
for factor in [10, 100, 1000, 10000]:
    chisq_min, Ndof = 1.1*factor, 1*factor
    rchisq, p, nsigma = assess_goodness_of_fit(chisq_min, Ndof)
    print("|        {0:.1f}             |      {1:d}        |        {2:.1f}          |      {3:.3f}        |        {4:.1f}         |".format(chisq_min, Ndof, rchisq, p, nsigma))
