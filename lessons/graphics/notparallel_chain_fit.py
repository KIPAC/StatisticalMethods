# Copied from LMC documentation
# Modified to use MPI (but not enable parallelization), to increase the parameter degeneracy, and to disperse the start points

# Here is a simple example. As shown it will run in non-parallel mode; comments indicate what to do for parallelization.

from lmc import *
## for MPI
from mpi4py import MPI
mpi_rank = MPI.COMM_WORLD.Get_rank()
from numpy.random import rand

### Define some parameters.
startx = [-10.0, -10.0, 10.0, 10.0]
starty = [-10.0, 10.0, -10.0, 10.0]
x = Parameter(name='x', value=startx[mpi_rank], width=0.1)
y = Parameter(name='y', value=starty[mpi_rank], width=0.1)

### This is the object that will be passed to the likelihood function.
### In this simple case, it just holds the parameter objects, but in general it could be anything.
### E.g., usually it would also contain or point to the data being used to constrain the model. A good idea is to write the state of any updaters to a file after each adaptation (using the on_adapt functionality), in which case keeping pointers to the updaters here is convenient. Also commonly useful: a DerivedParameter which holds the value of the posterior log-density for each sample.
class Thing:
    def __init__(self, x, y):
        self.x = x
        self.y = y
thing = Thing(x, y)

### The log-posterior function. Here we just assume a bivariate Gaussian posterior with marginal standard deviations s(x)=2 and s(y)=3, correlation coefficient 0.75, and means <x>=-1, <y>=1.
def post(thing):
    r = 0.99
    sx = 2.0
    sy = 3.0
    mx = -1.0
    my = 1.0
    return -0.5/(1.0-r**2)*( (thing.x()-mx)**2/sx**2 + (thing.y()-my)**2/sy**2 - 2.0*r*(thing.x()-mx)/sx*(thing.y()-my)/sy )

### Create a parameter space consisting of x and y, and associate the log-posterior function with it.
space = ParameterSpace([thing.x, thing.y], post)

### If we'd bothered to define a DerivedParameter in Thing which would hold the posterior density, we might want to define a larger ParameterSpace and pass it to the Engine later on to be saved in the Backends (instead of space).
#trace = ParameterSpace([thing.x, thing.y, thing.logP])

### Use slice sampling for robustness. Adapt the proposal distribution every 100 iterations starting with the 100th.
step = Metropolis()
parallel = None
## for MPI parallelization
#parallel = MPI.COMM_WORLD
## for parallelization via the filesystem, this would have to be set to a different value for each concurrently running instance
#parallel = 1
updater = MultiDimSequentialUpdater(space, step, 100, 100, parallel=parallel)

### Create an Engine and tell it to drive this Updater and to store the values of the free parameters.
engine = Engine([updater], space)

### Store the chain in a text file.
#chainfile = open("chain.txt", 'w')
## For filesystem parallelization, each instance should write to a different file.
## For MPI, the same is true, e.g.
chainfile = open("notparallel" + str(MPI.COMM_WORLD.Get_rank()) + ".txt", 'w')
backends = [ textBackend(chainfile) ]

### Print the chain to the terminal as well
#backends.append( stdoutBackend() )

### Run the chain for 10000 iterations
engine(10000, thing, backends)

### Close the text file to clean up.
chainfile.close()

## If this was a parallel run, print the convergence criterion for each parameter.
# print updater.R
