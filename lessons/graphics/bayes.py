from matplotlib import rc
import daft

rc("font", family="serif", size=12)
rc("text", usetex=True)

pgm = daft.PGM([2.4, 1.65], observed_style="inner")
pgm.add_node(daft.Node("alpha", r"$\alpha_0$", 0.25, 0.25, fixed=True))
pgm.add_node(daft.Node("beta", r"$\beta_0$", 0.25, 1.25, fixed=True))
pgm.add_node(daft.Node("mu", r"$\mu$", 1.0, 0.75))
pgm.add_node(daft.Node("N", r"$N$", 2.0, 0.75, observed=True))
pgm.add_edge("alpha", "mu")
pgm.add_edge("beta", "mu")
pgm.add_edge("mu", "N")
pgm.render()
pgm.figure.savefig("bayes_poissoneg_pgm.png", dpi=200)

pgm = daft.PGM([2.4, 1.65], observed_style="inner")
#pgm.add_node(daft.Node("prior", "prior", 0.25, 0.75, fixed=True))
pgm.add_node(daft.Node("mu", r"$\mu$", 1.0, 0.75))
pgm.add_node(daft.Node("N", r"$N$", 2.0, 0.75, observed=True))
#pgm.add_edge("prior", "mu")
pgm.add_edge("mu", "N")
pgm.render()
pgm.figure.savefig("bayes_poissoneg_pgm0.png", dpi=200)

