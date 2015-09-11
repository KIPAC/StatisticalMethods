import astropy.io.fits as pyfits
import numpy as np
import os


### definitions for modeling the data

def betaModelFun(r, x0, y0, S0, rc, beta):
    '''
    the fabled beta model
    '''
    return S0 * (1.0 + (r/rc)**2)**(-3.0*beta + 0.5)

def betaModelImage(xs, ys, x0, y0, S0, rc, beta):
    '''
    where xs and ys are arrays of x and y coordinate values, and the rest are beta model parameters
    Returns an image with values given by the (azimuthally symmetric) beta model parameters
    '''
    return betaModelFun(np.sqrt( (xs-x0)**2 + (ys-y0)**2 ), x0, y0, S0, rc, beta)

def modelImage(data, x0, y0, S0, rc, beta, bg):
    '''
    where xs and ys are arrays of x and y coordinate values, and the rest are beta model parameters
    The whole model
    '''
    return (betaModelImage(data.xs, data.ys, x0, y0, S0, rc, beta) + bg) * data.ex + data.bk



class XrayData:
    def __init__(self):
        ### download the data if we don't already have it
        targdir = 'a1835_xmm/'
        os.system('mkdir -p ' + targdir)
        imagefile = 'P0098010101M2U009IMAGE_3000.FTZ'
        expmapfile = 'P0098010101M2U009EXPMAP3000.FTZ'
        bkgmapfile = 'P0098010101M2X000BKGMAP3000.FTZ'
        remotedir = 'http://heasarc.gsfc.nasa.gov/FTP/xmm/data/rev0/0098010101/PPS/'
        for filename in [imagefile,expmapfile,bkgmapfile]:
            path = targdir + filename
            url = remotedir + filename
            if not os.path.isfile(path): # i.e. if the file does not exist already:
                os.system('wget -nd -O ' + path + ' ' + 'url')
        ### read in the data
        self.imfits = pyfits.open(targdir + imagefile)
        self.im = self.imfits[0].data
        self.bkfits = pyfits.open(targdir + bkgmapfile)
        self.bk = self.bkfits[0].data
        self.exfits = pyfits.open(targdir + expmapfile)
        self.ex = self.exfits[0].data
        ### make helper arrays of x and y coordinates
        self.xs = np.array([np.arange(self.im.shape[0]) for j in np.arange(self.im.shape[1])])
        self.ys = np.array([[j for i in np.arange(self.im.shape[1])] for j in np.arange(self.im.shape[0])])
        ### mask a list of non-cluster sources
        maskfile = 'M2ptsrc.txt'
        mask = np.loadtxt(targdir + maskfile)
        for reg in mask:
            for i in np.round(reg[1]+np.arange(-np.ceil(reg[2]),np.ceil(reg[2]))):
                for j in np.round(reg[0]+np.arange(-np.ceil(reg[2]),np.ceil(reg[2]))):
                    if (i-reg[1])**2 + (j-reg[0])**2 <= reg[2]**2:
                        self.ex[np.int(i-1), np.int(j-1)] = 0.0
        self.mask = self.ex * 0.0
        self.mask[self.ex > 0.0] = 1.0


def lnpost(params, data):
    # assumes S0 is a free parameter
    x0 = params[0]
    y0 = params[1]
    S0 = params[2]
    rc = params[3]
    beta = params[4]
    bg = params[5]
    if x0 < 0. or x0 >= data.im.shape[0] or y0 < 0. or y0 > data.im.shape[1] or S0 <= 0. or rc <= 0. or beta <= 0.0:
        return -np.inf
    mod = modelImage(data, x0, y0, S0, rc, beta, bg)
    if np.min(mod) <= 0.0:
        return -np.inf
    return np.sum( (-mod + data.im * np.log(mod)) * data.mask )

        
def lnpost2(params, data):
    # assumes log(S0) is a free parameter
    x0 = params[0]
    y0 = params[1]
    S0 = np.exp(params[2])
    rc = params[3]
    beta = params[4]
    bg = params[5]
    if x0 < 0. or x0 >= data.im.shape[0] or y0 < 0. or y0 > data.im.shape[1] or S0 <= 0. or rc <= 0. or beta <= 0.0:
        return -np.inf
    mod = modelImage(data, x0, y0, S0, rc, beta, bg)
    if np.min(mod) <= 0.0:
        return -np.inf
    return np.sum( (-mod + data.im * np.log(mod)) * data.mask )
