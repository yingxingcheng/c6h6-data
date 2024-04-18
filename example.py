import matplotlib.pyplot as plt
import numpy as np


def load_data(file_name, data_key):
    """
    Load data from a specified NPZ file.

    Parameters
    ----------
    file_name : str
        The path to the .npz file.
    data_key : str
        The key corresponding to the data array to be loaded from the file.

    Returns
    -------
    data : ndarray
        The data array stored under the specified key.
    """
    with np.load(file_name) as data:
        return data[data_key]


# Load the data
points = load_data("qm_data_c6h6.npz", "points")
density = load_data("qm_data_c6h6.npz", "density")

# Example: Plotting a slice where z=0
mask = points[:, 2] == 0
x = points[mask][:, 0]
y = points[mask][:, 1]
dens = density[mask]

plt.scatter(x, y, c=dens, cmap="viridis")
plt.colorbar(label="Electron Density")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Electron Density Distribution at Z=0")
plt.show()
