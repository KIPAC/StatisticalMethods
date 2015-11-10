#!/usr/bin/env python
#

# Description
"""
Utilities for doing example likelihood fitting
"""


__facility__ = "LikeFitUtils.py"
__abstract__ = __doc__
__author__    = "E. Charles"
__date__      = "$Date: 2014/07/10 21:51:02 $"
__version__   = "$Revision: 1.1 $, $Author: echarles $"
__release__   = "$Name:  $"

import numpy as np
import astropy.io.fits as pf
from scipy import optimize
from scipy import interpolate
import matplotlib.pyplot as plt


def LogPoisson(n_obs,n_pred):
    """ Returns the sum of negative log of the Poisson likelihood over all the bins

    n_obs      : array of the observed counts
    n_pred     : array of the predicted counts
    """
    return (n_pred - ( n_obs * np.log( n_pred ) )).sum()        


def CalcModelSum(norms,fixedModel,freeModels):
    """ Sum up the total number of model counts in each bin

    norms      : array of the normalizations of the freeModels
    fixedModel : array of the predicted counts for all the fixed model components
    freeModels : list of arrays of the predicted counts for each of the free model components

    returns an array with the sum of the model counts in each bin
    """
    if len(norms) != len(freeModels):
        print "Length of norm vector (%i) does not match number of free model components (%i)"%(len(norms),len(freeModels))
        return None

    sumModel = fixedModel.copy()
    for norm,freeModel in zip(norms,freeModels):
        sumModel += norm * freeModel
        pass
    return sumModel
   

def NLL(n_obs,norms,fixedModel,freeModels):
    """ Returns the negative log likelihood for a particular set of data and model parameters

    n_obs      : array of the observed counts
    norms      : array of the normalizations of the freeModels
    fixedModel : array of the predicted counts for all the fixed model components
    freeModels : list of arrays of the predicted counts for each of the free model components
    """
    n_pred = CalcModelSum(norms,fixedModel,freeModels)
    nll = LogPoisson(n_obs,n_pred)
    return nll


def NLL_func(n_obs,fixedModel,freeModels):
    """ Returns a function that calculates the NLL for a particular set of normalizations
    
    n_obs      : array of the observed counts
    fixedModel : array of the predicted counts for all the fixed model components
    freeModels : list of arrays of the predicted counts for each of the free model components
    """
    func = lambda x : NLL(n_obs,x,fixedModel,freeModels)
    return func


def NLL_func_profile(n_obs,pars,fix_par_mask,fixedModel,freeModels):
    """ Returns a function that calculates the NLL for a particular set of normalizations
    This allows you to fix some of the free models.

    n_obs      : array of the observed counts
    pars       : array of the best-fit parameters
    fix_par_mask : mask of which parameters to fix
    fixedModel : array of the predicted counts for all the fixed model components
    freeModels : list of arrays of the predicted counts for each of the free model components
    """
    newFixed = fixedModel.copy()
    newFreeModels = []
    
    for fix_par,par,freeModel in zip(fix_par_mask,pars,freeModels):
        if fix_par:
            newFixed += par * freeModel
        else:
            newFreeModels.append(freeModel)
    func = lambda x : NLL(n_obs,x,newFixed,newFreeModels)
    return func


def DeltaLL_func(nllFunc,nllMin,error_level=0):
    """ Returns a function that calculates the delta log-likelihood w.r.t. the mininum, 
    and possibly and offset error level

    nllFunc    : Function that calculates the NLL
    nllMin     : Minimum value of the NLL
    error_level: Offset, this can be used to solve for a particular error_level
    """
    func = lambda x : nllFunc(x) - nllMin - error_level
    return func


def Minimize(ftomin,init_pars):
    """ Uses scipy.optimize.fmin to minimize the NLL

    ftomin     : Function to minimize (basically NLL_func, above)
    init_pars  : array initial values of the fit parameters
    
    returns (fit_pars, nll_min, n_iter, n_calls, status)
    """
    result = optimize.fmin(ftomin,init_pars,full_output=1,disp=0)
    return result


def ParameterScan(ftomin,par_sets):
    """ This calculates the NLL for a series of parameter sets.
    Note that it does not re-optimize the parameter, i.e., this
    is NOT a profile likelihood.   

    ftomin      : the NLL function, takes an array(npar) as input
    pars_sets   : an array of n x npar parameters
    
    returns an array(n) of NLL values
    """
    retVals = np.zeros((len(par_sets)))
    for i,pars in enumerate(par_sets):
        retVals[i] = ftomin(pars)
        pass
    return retVals


def ProfileScan(n_obs,par_sets,fix_par_mask,fixedModel,freeModels):
    """ This calculates the NLL for a series of parameter sets.
    Note that it does re-optimize the parameter, i.e., this
    IS a profile likelihood.   

    n_obs      : array of the observed counts
    pars_sets  : an array of n x npar parameters
    fix_par_mask : mask of which parameters to fix, an array(npar,'bool')
    fixedModel : array of the predicted counts for all the fixed model components
    freeModels : list of arrays of the predicted counts for each of the free model components
  
    returns an array(n) of NLL values
    """
    retVals = np.zeros((len(par_sets)))
    freeParMask = np.invert(fix_par_mask)
    for i,pars in enumerate(par_sets):
        ftomin = NLL_func_profile(n_obs,pars,fix_par_mask,fixedModel,freeModels)
        result = Minimize(ftomin,pars[freeParMask])
        retVals[i] = result[1]
        pass
    return retVals


def MakeParSets_1DScan(basepars,par_index,minval,maxval,nstep,log=False):
    """ This makes a set of parameter vectors appropriate to a 1D scan
    (i.e., a scan over a particular parameter)

    basepars   : The baseline values of the parameters
    minval     : The minimum parameter value
    maxval     : The maximum paramter value
    nstep      : The number of paramter steps to take
    log        : Logrithmic or linear steps
    """
    if log:
        vals = np.logspace(np.log10(minval), np.log10(maxval), nstep)
    else:        
        vals = np.linspace(minval,maxval,nstep)
    
    l = []
    for val in vals:
        xv = basepars.copy()
        xv[par_index] = val
        l.append(xv)
        pass

    par_sets = np.vstack(l)
    return par_sets


def BuildInterpolator(par_sets,par_index,delta_nll_vals):
    """ Build an interpolator using the results of a parameter scan

    par_sets   : The sets of paramters scaned over
    par_index  : The index of the parameter of interest
    delta_nll_vals  : The correspond delta NLL values (w.r.t. minimum value)

    returns a callable, 1D, linear scipy.interpolate.interp1d object 
    """
    xvals = par_sets[0:,par_index]
    yvals = delta_nll_vals
    interp = interpolate.interp1d(xvals,yvals)
    return interp


def SolveForErrorLevel(func,nll_min,error_level,mle,xbounds,posError=True):
    """ Use a functional to solve for a particular error level,
    i.e., the parameter value where the NLL changes by a particular amount

    func         : The functional (either the NLL_Func or the interpolator)   
    nll_min      : The minimum value of the NLL
    error_level  : The requested error level
    mle          : The maximum likelihood estimate, i.e., the value of the parameter that maximize the likelihood
    xbounds      : The bounds on the parameter
    pos_error    : If true results the positive side error, if false returns the negative side error

    returns the parameter value correspond to the given error level (not that this is not the uncertaintity, but 
    rather the mle +/- the uncertainty)
    """
    eq_to_solve = DeltaLL_func(func,nll_min,error_level)
    if posError:
        minval = mle
        maxval = xbounds[1]
    else:
        minval = xbounds[0]
        maxval = mle        

    try:
        result = optimize.brentq(eq_to_solve,minval,maxval)
    except:
        print "Failed to find root",minval,maxval,eq_to_solve(minval),eq_to_solve(maxval)
        return None

    return result


def PlotNLLScan(normVals,nllVals):
    """ Plots the results of a scan of NLL versus Flux

    normVals:   The flux normalization values
    nllVals:    The corresponding value of the NLL
    
    returns a pyplot figure and axes
    """
    figure = plt.figure()
    ax = figure.add_subplot(111)
    ax.set_xlabel('Flux')
    ax.set_ylabel(r"$-\Delta \log \mathcal{L}$")
    ax.set_xlim(0.,2.)
    ax.set_ylim(-10.,1.)
    ax.plot(normVals,nllVals,'-',color='r',label='NLL')
    return figure,ax


def LoadFromFitsFile(fileName):
    """ Opens a fits file and loads in the data and model templates

    fileName   : Name of the input file
    returns a dict of name : array
    """
    fin = pf.open(fileName)
    retDict = {}
    retDict["DATA"] = fin[0].data.swapaxes(0,2)

    for hdu in fin[3:]:
        retDict[hdu.name] = hdu.data.swapaxes(0,2)
        pass

    return retDict


if __name__=='__main__':

    # Ok, read in the input data
    inputDict = LoadFromFitsFile("data/draco_srcTemplates.fits")

    # Parse out the bits we need
    n_obs = inputDict["DATA"]  # This is the actual data
    fixed = inputDict["FIXED"]  # This is the sum of the fixed model components
    modelList = [ inputDict["DRACO"], inputDict["GLL_IEM_V06"] ] # These are the free model components
    par_index = 0 # This is the index of the parameter we care about

    ftomin = NLL_func(n_obs,fixed,modelList)
    init_pars = np.ones((2))

    result = Minimize(ftomin,init_pars)
    mle_pars = result[0]
    mle = mle_pars[par_index]
    nll_min = result[1]

    fix_par_mask = np.zeros((2),'?')
    fix_par_mask[par_index] = True

    par_bounds = (1e-2,2.0)
    nsteps = 25

    par_sets = MakeParSets_1DScan(mle_pars,par_index,par_bounds[0],par_bounds[1],nsteps,log=True)

    pf1 = ProfileScan(n_obs,par_sets,fix_par_mask,fixed,modelList)
    pf2 = ParameterScan(ftomin,par_sets)

    interp1 = BuildInterpolator(par_sets,par_index,pf1)
    interp2 = BuildInterpolator(par_sets,par_index,pf2)

    lim1 = SolveForErrorLevel(interp1,nll_min,1.35,mle,par_bounds)
    lim2 = SolveForErrorLevel(interp2,nll_min,1.35,mle,par_bounds)
 
    fig1,ax1 = PlotNLLScan(par_sets[0:,par_index],nll_min-pf1)

    ax1.plot(par_sets[0:,par_index],nll_min-pf2,'-',color='b',label='Profile')
    ax1.hlines(-1.35,0,2.0,linestyles=u'dotted')
    ax1.vlines(lim1,-10,1,linestyles=u'dashed')
    
    ax1.legend()
    #plt.show()
