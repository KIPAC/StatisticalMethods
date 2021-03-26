import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import LogStretch
logstretch = LogStretch()

class Image:
    def __init__(self, imdata, exdata, imx=None, imy=None):
        self.im = imdata
        self.ex = exdata
        if imx is None or imy is None:
            # NOTE order of x and y here - this gets us something consistent with the FITS convention
            # add 1 to make IMAGE coordinates
            self.imx, self.imy = np.meshgrid(np.arange(imdata.shape[0])+1, np.arange(imdata.shape[1])+1)
        else:
            self.imx = imx
            self.imy = imy
    def cutout(self, x0, x1, y0, y1):
        # Again, NOTE order of x and y. y goes into the FIRST index.
        # Also note that the arguments are meant to be IMAGE coordinates, indexed starting from 1
        return Image(self.im[(y0-1):y1,(x0-1):x1], self.ex[(y0-1):y1,(x0-1):x1], 
                     self.imx[(y0-1):y1,(x0-1):x1], self.imy[(y0-1):y1,(x0-1):x1])
    def extent(self):
        return [np.min(self.imx), np.max(self.imx), np.min(self.imy), np.max(self.imy)]
    def display(self, log_image=True):
        fig, ax = plt.subplots(1,2);
        extent = self.extent()
        if log_image:
            ax[0].imshow(logstretch(self.im), cmap='gray', origin='lower', extent=extent);
            ax[0].set_title('image (log scale)');
        else:
            ax[0].imshow(self.im, cmap='gray', origin='lower', extent=extent);
            ax[0].set_title('image');
        ax[1].imshow(self.ex, cmap='gray', origin='lower', extent=extent);
        ax[1].set_title('exposure map');
