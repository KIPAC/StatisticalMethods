import astropy.io.fits as pyfits
import numpy as np
import os

# ====================================================================

# Functions for realizing the model:

def beta_model_profile(r, S0, rc, beta):
    '''
    The fabled beta model, radial profile S(r)
    '''
    return S0 * (1.0 + (r/rc)**2)**(-3.0*beta + 0.5)

def beta_model_image(x, y, x0, y0, S0, rc, beta):
    '''
    Here, x and y are arrays ("meshgrids" or "ramps") containing x and y pixel numbers,
    and the other arguments are galaxy cluster beta model parameters.
    Returns a surface brightness image of the same shape as x and y.
    '''
    return beta_model_profile(np.sqrt((x-x0)**2 + (y-y0)**2), S0, rc, beta)

def model_image(x, y, ex, pb, x0, y0, S0, rc, beta, b):
    '''
    Here, x, y, ex and pb are images, all of the same shape, and the other args are
    cluster model and X-ray background parameters. ex is the (constant) exposure map
    and pb is the (constant) particle background map.
    '''
    return (beta_model_image(x, y, x0, y0, S0, rc, beta) + b) * ex + pb

# ====================================================================

class XrayData:

    def __init__(self):
        self.pars = np.zeros(6)
        return


    def read_in_data(self):
        # Download the data if we don't already have it
        self.targdir = 'a1835_xmm/'
        os.system('mkdir -p ' + self.targdir)
        imagefile = 'P0098010101M2U009IMAGE_3000.FTZ'
        expmapfile = 'P0098010101M2U009EXPMAP3000.FTZ'
        bkgmapfile = 'P0098010101M2X000BKGMAP3000.FTZ'
        remotedir = 'http://heasarc.gsfc.nasa.gov/FTP/xmm/data/rev0/0098010101/PPS/'
        for filename in [imagefile,expmapfile,bkgmapfile]:
            path = self.targdir + filename
            url = remotedir + filename
            if not os.path.isfile(path): # i.e. if the file does not exist already:
                os.system('wget -nd -O ' + path + ' ' + 'url')

        # Read in the data
        self.imfits = pyfits.open(self.targdir + imagefile)
        self.im = self.imfits[0].data
        self.pbfits = pyfits.open(self.targdir + bkgmapfile)
        self.pb = self.pbfits[0].data
        self.exfits = pyfits.open(self.targdir + expmapfile)
        self.ex = self.exfits[0].data

        return


    def set_up_maps(self):

        # Make x and y ramps
        self.x = np.array([np.arange(self.im.shape[0]) for j in np.arange(self.im.shape[1])])
        self.y = np.array([[j for i in np.arange(self.im.shape[1])] for j in np.arange(self.im.shape[0])])

        ### mask a list of circular regions covering non-cluster sources
        maskfile = 'M2ptsrc.txt'
        mask = np.loadtxt(self.targdir + maskfile)
        for reg in mask:
            distance2 = (self.x-(reg[0]-1.0))**2 + (self.y-(reg[1]-1.0))**2
            self.ex[distance2 <= reg[2]**2] = 0.0
        # helpful mask image to keep track of which pixels we can ignore
        self.mask = self.ex * 0.0
        self.mask[self.ex > 0.0] = 1.0

        return


    def set_pars(self,x0,y0,S0,rc,beta,b):
        self.pars[0] = x0
        self.pars[1] = y0
        self.pars[2] = S0
        self.pars[3] = rc
        self.pars[4] = beta
        self.pars[5] = b
        return


    def make_mean_image(self):
        x0 = self.pars[0]
        y0 = self.pars[1]
        S0 = self.pars[2]
        rc = self.pars[3]
        beta = self.pars[4]
        b = self.pars[5]
        self.mu = model_image(self.x,self.y,self.ex,self.pb,x0,y0,S0,rc,beta,b)
        return


    def make_mock_data(self):
        self.mock = np.random.poisson(self.mu,self.mu.shape)
        return


    def evaluate_log_prior(self):
        # Uniform in all parameters...
        return 0.0


    def evaluate_log_likelihood(self):
        self.make_mean_image()
        # Return un-normalized Poisson sampling distribution:
        # log (\mu^N e^{-\mu} / N!) = N log \mu - \mu + constant
        return np.sum(self.im * np.log(self.mu) - self.mu)


    def evaluate_unnormalised_log_posterior(self,x0,y0,S0,rc,beta,b):
        self.set_pars(x0,y0,S0,rc,beta,b)
        return self.evaluate_log_likelihood() + self.evaluate_log_prior()



# ====================================================================
'''

Adam's routines for input into MCMC:

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
'''
