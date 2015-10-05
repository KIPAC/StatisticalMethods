import daft

def draw():

    # Instantiate a PGM.
    pgm = daft.PGM([3.3, 3.0], origin=[0.3, 0.3], grid_unit=2.6, node_unit=1.3, observed_style="inner")

    # Model parameters:
    pgm.add_node(daft.Node("m", r"$m$", 0.8, 2.8))
    pgm.add_node(daft.Node("b", r"$b$", 1.8, 2.8))

    # Latent variable - intrinsic or true y:
    pgm.add_node(daft.Node("ytrue", r"$y^{\rm true}_k$", 1.3, 1.4, fixed=True, offset=(10,-25)))

    # Data - observed y:
    pgm.add_node(daft.Node("y", r"$y_k$", 2.5, 1.4, observed=True))

    # Constants - x and errors:
    pgm.add_node(daft.Node("sigma", r"$\sigma_k$", 1.9, 0.9, fixed=True, offset=(-3,0)))
    pgm.add_node(daft.Node("x", r"$x_k$", 0.8, 1.1, fixed=True))

    # Add in the edges.
    pgm.add_edge("m", "ytrue")
    pgm.add_edge("x", "ytrue")
    pgm.add_edge("b", "ytrue")
    pgm.add_edge("sigma", "y")
    pgm.add_edge("ytrue", "y")

    # And a plate for the pixels
    pgm.add_plate(daft.Plate([0.5, 0.7, 2.7, 1.4], label=r"datapoints $k$", shift=-0.1))

    # Render and save.
    pgm.render()
    pgm.figure.savefig("straightline_pgm.png", dpi=300)

    return
