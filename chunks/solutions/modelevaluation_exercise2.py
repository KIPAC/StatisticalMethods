"""
The evidence integral involves a Gaussian likelihood (red) integrated over a
uniform prior (blue): the evidence can be shown to be given by E = f x L_max
where L_max} is the maximum value of the likelihood, and f is _the fraction of
the area under the blue dashed curve that is shaded red_. f is 0.31, 0.98, and
0.07 in the left, center and righthand cases.
"""

from IPython.display import Image
Image('../graphics/evidence.png')
