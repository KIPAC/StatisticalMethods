# MCMC packages

An incomplete listing of potentially useful `Python` packages that perform Markov Chain Monte Carlo:

Code | Algorithm | Bonus link
---- | --------- | -----
[`emcee`](http://dan.iel.fm/emcee/current/) | Goodman-Weare | [paper](http://arxiv.org/abs/1202.3665)
[`kombine`](http://home.uchicago.edu/~farr/kombine/index.html) | briefly tempered Metropolis-Hastings | [paper](https://arxiv.org/abs/1309.7709)
[`lmc`](https://github.com/abmantz/lmc) | Metropolis-Hastings, Goodman-Weare |
[`MultiNest`](https://github.com/JohannesBuchner/PyMultiNest) | nested sampling | papers [1](http://arxiv.org/abs/0809.3437) [2](http://arxiv.org/abs/1306.2144)
[`pymc`](https://github.com/pymc-devs/pymc) | Metropolis-Hastings | 
[`pymc3`](https://github.com/pymc-devs/pymc3) | Metropolis-Hastings, HMC |
[`PyStan`](http://mc-stan.org) | HMC |

For `R` users, there are numerous options on [CRAN](https://cran.r-project.org/), but we list only a couple that we know or have heard of being used:

Code | Algorithm | Bonus link
---- | --------- | -----
[`rgw`](https://github.com/abmantz/rgw) | Goodman-Weare | [CRAN](https://cran.r-project.org/package=rgw)
[`LaplacesDemon`](https://github.com/LaplacesDemonR/LaplacesDemon) | many | [CRAN](https://cran.r-project.org/package=LaplacesDemon)
[`RStan`](http://mc-stan.org) | HMC |

Gibbs samplers that analyze models to determine conjugacy relations (some have `Python`/`R` interfaces):

* [BUGS](http://openbugs.net/w/FrontPage)
* [JAGS](http://mcmc-jags.sourceforge.net/)


Gibbs samplers specifically for linear regression:

Code | Language | multiple $x$'s | multiple $y$'s
---- | :------: | :------------: | :------------:
[`linmix_err`](http://idlastro.gsfc.nasa.gov/ftp/pro/math/linmix_err.pro) | IDL | no | no
[`mlinmix_err`](http://idlastro.gsfc.nasa.gov/ftp/pro/math/mlinmix_err.pro) | IDL | yes | no
[`linmix`](https://github.com/jmeyers314/linmix) | Python | no | no
[`lrgs`](https://github.com/abmantz/lrgs) | R, Python | yes | yes
