import daft


def simple():

    # Instantiate a PGM.
    pgm = daft.PGM([3.3, 3.0], origin=[0.3, 0.3], grid_unit=2.6, node_unit=1.3, observed_style="inner")

    # Model parameters:
    pgm.add_node(daft.Node("a", r"$a$", 0.8, 2.8))
    pgm.add_node(daft.Node("b", r"$b$", 1.8, 2.8))

    # Latent variable - intrinsic magnitude:
    pgm.add_node(daft.Node("m", r"$m_k$", 1.3, 1.4, fixed=True, offset=(0,-25)))

    # Data - observed magnitude:
    pgm.add_node(daft.Node("mobs", r"$m^{\rm obs}_k$", 2.5, 1.4, observed=True))

    # Constants - magnitude errors:
    pgm.add_node(daft.Node("merr", r"$\sigma_k$", 1.9, 0.9, fixed=True, offset=(-3,0)))

    # Add in the edges.
    pgm.add_edge("a", "m")
    pgm.add_edge("b", "m")
    pgm.add_edge("merr", "mobs")
    pgm.add_edge("m", "mobs")

    # And a plate for the pixels
    pgm.add_plate(daft.Plate([0.5, 0.7, 2.7, 1.4], label=r"cepheids $k$", shift=-0.1))

    # Render and save.
    pgm.render()
    pgm.figure.savefig("cepheids_pgm.png", dpi=300)

    return


# Just make the PGM:

pgm()
