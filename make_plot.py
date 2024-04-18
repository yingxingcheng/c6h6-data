#!/usr/bin/env python


import matplotlib.pyplot as plt
import numpy as np

"""
The script is to show how to use the data generated form `Part-Cube` program.
"""


def load_data(dens_type):
    """
    Load density data for a specific type from a .npz file.

    Parameters
    ----------
    dens_type : str
        The key within the .npz file to load. Expected keys include "density" and
        "isolated_density".

    Returns
    -------
    x : ndarray
        Array of x coordinates.
    y : ndarray
        Array of y coordinates.
    dens : ndarray
        Array of density values corresponding to the x and y coordinates.
    shape : tuple
        Shape of the full density grid, as stored in the file.

    Raises
    ------
    AssertionError
        If the number of unique x or y values does not match the expected dimensions from `shape`.
    """
    fname = "qm_data_c6h6.npz"
    data = np.load(fname)
    points = data["points"]
    shape = data["shape"]
    mask = points[:, 2] == 0.0
    plane = points[mask][:, :-1]
    dens = data[dens_type][mask]
    assert plane.shape[0] == dens.shape[0]
    x = plane[:, 0]
    y = plane[:, 1]
    assert len(set(x)) == shape[0] and len(set(y)) == shape[1]
    return x, y, dens, shape


def plot_scatter(dens_type):
    """
    Create a scatter plot of density data.

    Parameters
    ----------
    dens_type : str
        The type of density data to plot.

    Notes
    -----
    The output scatter plot is saved as a PDF file named `c6h6_scatter_{dens_type}.pdf`.
    """
    x, y, dens, _ = load_data(dens_type)
    fig, ax = plt.subplots(figsize=(4, 4))
    plt.scatter(x, y, s=dens)
    plt.tight_layout()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.tight_layout()
    plt.savefig(f"c6h6_scatter_{dens_type}.pdf")


def plot_matshow(dens_tyep):
    """
    Create a matrix-style plot of the logarithm of density data.

    Parameters
    ----------
    dens_type : str
        The type of density data to plot.

    Notes
    -----
    The output matrix plot is saved as a PDF file named `c6h6_matshow_{dens_type}.pdf`.
    """
    _, _, dens, shape = load_data(dens_type)
    fig, ax = plt.subplots(figsize=(6, 4))
    dens_mat = dens.reshape(shape[:-1])
    # dens_mat = np.clip(dens_mat, 0, 0.9)
    dens_mat = np.log(dens_mat + 1e-10)
    cax = ax.matshow(dens_mat)
    cbar = fig.colorbar(cax, ax=ax, fraction=0.04, pad=0.04)
    cbar.set_label(r"$\log(\rho(x,y,z=0) + 10^{-10})$")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.tight_layout()
    plt.savefig(f"c6h6_matshow_{dens_type}.pdf")


def plot_contour(dens_type):
    """
    Create a contour plot of density data.

    Parameters
    ----------
    dens_type : str
        The type of density data to plot.

    Notes
    -----
    The output contour plot is saved as a PDF file named `c6h6_contour_{dens_type}.pdf`.
    """
    x, y, dens, shape = load_data(dens_type)
    fig, ax = plt.subplots(figsize=(4, 4))
    # Note: the reason is that the meshgrid is constructed with `indexing=ij`
    Z = dens.reshape((shape[0], shape[1]))
    X = x.reshape((shape[0], shape[1]))
    Y = y.reshape((shape[0], shape[1]))
    levels = np.linspace(0, 25, 2000)
    plt.contour(X, Y, Z, levels=levels, linewidths=0.5)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.tight_layout()
    plt.savefig(f"c6h6_contour_{dens_type}.pdf")


if __name__ == "__main__":
    for dens_type in ["density", "isolated_density"]:
        plot_scatter(dens_type)
        plot_matshow(dens_type)
        plot_contour(dens_type)
