import daft


def forward():

    # Instantiate a PGM.
    pgm = daft.PGM([3.3, 3.0], origin=[0.3, 0.3], grid_unit=2.6, node_unit=1.3, observed_style="inner")

    # Model parameters.
    pgm.add_node(daft.Node("theta", r"$\theta$", 1.7, 2.8, fixed=True))

    # Latent variable: Poisson mean in kth pixel
    pgm.add_node(daft.Node("mean", r"$\mu_k$", 1.7, 1.7, fixed=True, offset=(-12,0)))

    # Constants - ex and pb
    pgm.add_node(daft.Node("ex", r"ex$_k$", 0.9, 1.7, fixed=True))
    pgm.add_node(daft.Node("pb", r"pb$_k$", 1.3, 1.1, fixed=True, offset=(-8,0)))

    # Data - counts in kth pixel:
    pgm.add_node(daft.Node("counts", r"$N_k$", 2.7, 1.7))

    # Add in the edges.
    pgm.add_edge("theta", "mean")
    pgm.add_edge("ex", "mean")
    pgm.add_edge("pb", "mean")
    pgm.add_edge("mean", "counts")

    # And a plate for the pixels
    pgm.add_plate(daft.Plate([0.5, 0.7, 2.7, 1.7], label=r"pixels $k$", shift=-0.1))

    # Render and save.
    pgm.render()
    pgm.figure.savefig("cluster_pgm_forward.png", dpi=300)

    return


def inverse():

    # Instantiate a PGM.
    pgm = daft.PGM([3.3, 3.0], origin=[0.3, 0.3], grid_unit=2.6, node_unit=1.3, observed_style="inner")

    # Model parameters.
    pgm.add_node(daft.Node("theta", r"$\theta$", 1.7, 2.8))

    # Latent variable: Poisson mean in kth pixel
    pgm.add_node(daft.Node("mean", r"$\mu_k$", 1.7, 1.7, fixed=True, offset=(-12,0)))

    # Constants - ex and pb
    pgm.add_node(daft.Node("ex", r"ex$_k$", 0.9, 1.7, fixed=True))
    pgm.add_node(daft.Node("pb", r"pb$_k$", 1.3, 1.1, fixed=True, offset=(-8,0)))

    # Data - counts in kth pixel:
    pgm.add_node(daft.Node("counts", r"$N_k$", 2.7, 1.7, observed=True))

    # Add in the edges.
    pgm.add_edge("theta", "mean")
    pgm.add_edge("ex", "mean")
    pgm.add_edge("pb", "mean")
    pgm.add_edge("mean", "counts")

    # And a plate for the pixels
    pgm.add_plate(daft.Plate([0.5, 0.7, 2.7, 1.7], label=r"pixels $k$", shift=-0.1))

    # Render and save.
    pgm.render()
    pgm.figure.savefig("cluster_pgm_inverse.png", dpi=300)

    return
