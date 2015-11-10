#!/usr/bin/env python
#

# Description
"""
Utilities for doing example SED manipulation
"""


__facility__ = "SedUtils.py"
__abstract__ = __doc__
__author__    = "E. Charles"
__date__      = "$Date: 2014/07/10 21:51:02 $"
__version__   = "$Revision: 1.1 $, $Author: echarles $"
__release__   = "$Name:  $"

import yaml
import numpy as np
from scipy import optimize
from scipy import interpolate
import matplotlib.pyplot as plt

import LikeFitUtils as lfu

class SedBin:
    """ This is a small utility class to look up the log-likelihood for a given flux in an energy bin
    """
    def __init__(self,sedDict):
        """ C'tor, takes a results dictionary as defined in the *_sed.yaml file
        """
        self.emin = sedDict["emin"]
        self.emax = sedDict["emax"]
        self.emean = np.sqrt(self.emin*self.emax)
        self.ewidth = self.emax - self.emin
        self.eflux2npred = sedDict["eflux2npred"]
        self.flux = sedDict["flux"]
        self.eflux = sedDict["eflux"]
        self.logLike = sedDict["logLike"]
        self.interp = interpolate.interp1d(self.flux,self.logLike,bounds_error=True,fill_value=-1e5)

        
    def __call__(self,fluxVal):
        """ Return the log-likelihood for a given flux value
        """ 
        return self.interp(fluxVal)


    def logLikeFromEFlux(self,efluxVal):
        """ Return the log-likelihood for a given energy flux value
        """
        fluxVal = efluxVal / self.emean
        return self.interp(fluxVal)


class SED:
    """ This is a small utility class to add together the log-likelihoods for several energy bins
    """
    def __init__(self,sedBinList):
        """ C'tor, takes a list of results dictionaries as defined in the *_sed.yaml file
        """
        self.binList = []
        self.nBin = len(sedBinList)
        self.energyBins = np.zeros((self.nBin+1))    
        for i,sedBinDict in enumerate(sedBinList):
            sedBin = SedBin(sedBinDict)
            self.binList.append(sedBin)
            self.energyBins[i] = sedBin.emin
            pass
        self.energyBins[-1] = sedBin.emax
        self.binByBinUls = None

    def __call__(self,fluxVals):
        """ Return the log-likelihood for a spectrum (i.e., a set of flux values for the various energy bins)
        """
        retVal = 0.
        for bin,fluxVal in zip(self.binList,fluxVals):
            if fluxVal < 0:
                retVal += 100.
            else:
                retVal -= bin(fluxVal)
            pass
        return retVal


    def NLL_func(self,fluxVals):
        """ Returns a function of a single normalization paramter that can be passed to a minimizer
        
        fluxVals   :   The baseline flux values, we will be fitting for a globlal scale factor w.r.t. these values           
        """
        func = lambda x : self(x*fluxVals)
        return func


    def Minimize(self,fluxVals,x0):
        """ Minimize the negative log-likelihood w.r.t. an overall scale factor, given an input spectrum
        
        fluxVals   :   The baseline flux values, we will be fitting for a globlal scale factor w.r.t. these values           
        x0         :   Initial value for the global scale factor

        returns a scipy.optimize result object
        """
        ftomin = self.NLL_func(fluxVals)
        result = optimize.fmin(ftomin,[x0],full_output=1,disp=0)
        return result


    def BinByBinULs(self):
        """ Calculat the 95% CL Upper limits in each energy bin and return them
        """
        if self.binByBinUls is not None:
            return self.binByBinUls
        self.binByBinUls = np.ndarray((self.nBin))
        for i,sedBin in enumerate(self.binList):
            xbounds = (sedBin.interp.x[0],sedBin.interp.x[-1])
            xinit = sedBin.interp.x[-1]*sedBin.interp.x[-1]
            result = optimize.fmin(sedBin,[xinit],full_output=1,disp=0)
            mle = result[0][0]
            nll_min = result[1]
            ul95 = lfu.SolveForErrorLevel(sedBin,nll_min,-1.35,mle,xbounds)
            self.binByBinUls[i] = ul95
            pass
        return self.binByBinUls


def PlotSED(eBins,uls,bandDict=None):
    """ Make a plot of the Spectral Energy Distribution.
    
    In fact this just plots the values as upper limits
    
    eBins    : The energy bin edges
    uls      : The corresponding upper limits
    bandDict : An optional dictionary with the expected upper limit quantiles for the Brazil bands
    """
    figure = plt.figure()
    ax = figure.add_subplot(111)
    ax.set_xlabel("E [MeV]")
    ax.set_ylabel(r"Energy Flux 95% CL UL [$MeV cm^{-2} s^{-1}$]")
    ax.set_xlim(eBins[0],eBins[-1])
    ax.set_ylim(1e-8,1e-4)
    ax.set_xscale('log')
    ax.set_yscale('log',nonposy='clip')

    xvals = np.sqrt(eBins[0:-1]*eBins[1:])
    xerr = np.array([xvals-eBins[0:-1],eBins[1:]-xvals])
    yvals = xvals*uls
    yerr = np.array([0.5*yvals,yvals-yvals])
       
    if bandDict:   
        ax.fill_between(xvals,np.array(bandDict['q05']),np.array(bandDict['q95']),color='y',label='2sigma')    
        ax.fill_between(xvals,np.array(bandDict['q16']),np.array(bandDict['q84']),color='g',label='1sigma')
        ax.loglog(xvals,np.array(bandDict['q50']),ls='--',color='black',label='Median')

    ax.errorbar(xvals, yvals, yerr=yerr, uplims=True, lw=1, color='black', ls='none', zorder=1)
    ax.errorbar(xvals, yvals, xerr=xerr, lw=1.35, color='black', ls='none', zorder=2, capsize=0)

    return figure,ax



def PlotLimits(masses,uls,bandDict=None):
    """ Make a plot of the upper limits as a function of mass for a DM channel
    
    
    masses   : The mass values (in GeV)
    uls      : The corresponding upper limits
    bandDict : An optional dictionary with the expected upper limit quantiles for the Brazil bands
    """
    figure = plt.figure()
    ax = figure.add_subplot(111)
    ax.set_xlabel(r"$m_{\chi}$ [GeV]")
    ax.set_ylabel(r"$\langle \sigma v \rangle$ 95% CL UL")
    ax.set_xlim(masses[0],masses[-1])
    ax.set_ylim(1e-27,1e-22)
    if bandDict:
        ax.fill_between(masses,np.array(bandDict['q05']),np.array(bandDict['q95']),color='y',label='2sigma')
        ax.fill_between(masses,np.array(bandDict['q16']),np.array(bandDict['q84']),color='g',label='1sigma')
        ax.loglog(masses,np.array(bandDict['q50']),ls='--',color='black',label='Median')
    ax.loglog(masses,uls*1e-26,ls='-',color='r',label='NLL')
    return figure,ax
    


if __name__=='__main__':

    sedData = yaml.load(open("results/draco_sed.yaml"))
    sed = SED(sedData)

    dmSpectra = yaml.load(open("ancil/DM_spectra.yaml"))

    xbounds = (1e-4,1e6)
    error_level = 1.35


    """
    sed_uls = sed.BinByBinULs()
    fig,ax = PlotSED(sed.energyBins,sed_uls)
    """


    resultDict = {}

    # Loop over channels
    for chan,chanDict in dmSpectra.items():
        nMass = len(chanDict)
        mle = np.ndarray((nMass))
        nll  = np.ndarray((nMass))
        ts  = np.ndarray((nMass))
        ul  = np.ndarray((nMass))
        # Loop over masses, but we want to keep things in order
        masses = chanDict.keys()
        masses.sort()
        for i,mass in enumerate(masses):
            fluxVals = chanDict[mass]
            print "Working on %s channel at %.1f GeV"%(chan,mass)
            nll_func = sed.NLL_func(fluxVals)
            result = sed.Minimize(fluxVals,1.0)
            mle[i] = result[0][0]
            nll[i] = result[1]
            nll_null = nll_func(0)
            ts[i] = 2.*(nll_null-nll[i])
            ul[i] = lfu.SolveForErrorLevel(nll_func,nll[i],error_level,mle[i],xbounds)
            pass
        resultDict[chan] = {"Masses":masses,
                            "MLE":mle,
                            "NLL":nll,
                            "TS":ts,
                            "UL95":ul}
        pass

    out = open("results/draco_dm_results.yaml",'w!')
    out.write( yaml.dump(resultDict) )
    out.close()

    
    
    bands = yaml.load(open("ancil/draco_spectral_mc_bands.yaml"))            
    a,f = PlotLimits(resultDict['bb']['Masses'],resultDict['bb']['UL95'],bands['bb']['ulimits'])
