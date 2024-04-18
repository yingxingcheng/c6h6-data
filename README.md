
# Data Documentation

## Overview

The `qm_data_c6h6.npz` file is a compressed NumPy data file used in quantum mechanical simulations or calculations specific to benzene (C6H6). This file stores various density matrices and related quantum properties on a grid of points in space. It is primarily intended for visualization and analysis of the electron density and other associated metrics at a fine-grained level.

## File Contents

The `qm_data_c6h6.npz` file typically contains the following arrays:

- **`points`**: A 2D array where each row represents the coordinates `(x, y, z)` of a point in the grid.
- **`shape`**: The shape or dimensions of the 3D grid from which the 2D plane data is extracted.
- **`density`**: Electron density values corresponding to each point in `points`.
- **`isolated_density`**: Density values for isolated systems, if available, corresponding to the points.

Each array is stored as a key-value pair in the file, where the key is the name of the array (e.g., "points", "density").

## Requirements

To use the `qm_data_c6h6.npz` file effectively, you need:

- **Python**: A recent version (Python 3.7 or newer is recommended).
- **NumPy**: For handling arrays and data manipulation.
- **Matplotlib**: For data visualization.

## How to Load Data

To load data from the `qm_data_c6h6.npz` file, you can use the following Python function as an example:

```python
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
```

## Example Usage

Here's how you might typically use the `qm_data_c6h6.npz` file in a Python script:

```python
import numpy as np
import matplotlib.pyplot as plt

# Load the data
points = load_data('qm_data_c6h6.npz', 'points')
density = load_data('qm_data_c6h6.npz', 'density')

# Example: Plotting a slice where z=0
mask = points[:, 2] == 0
x = points[mask][:, 0]
y = points[mask][:, 1]
dens = density[mask]

plt.scatter(x, y, c=dens, cmap='viridis')
plt.colorbar(label='Electron Density')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Electron Density Distribution at Z=0')
plt.show()
```

## Introduction to `make_plot.py`

### Purpose

The `make_plot.py` script is designed to utilize the data from the `qm_data_c6h6.npz` file to create visualizations that represent various types of density distributions for benzene.
It provides functions to generate scatter plots, matrix-style plots, and contour plots, each illustrating different aspects of the electron density or isolated electron density on a predefined grid.

### Functions

The script contains the following key functions:

- **`load_data(dens_type)`**: Loads data for a specified type of density from the `.npz` file. This function is critical for retrieving and preparing data points for visualization.
- **`main_scatter(dens_type)`**: Generates scatter plots showing the spatial distribution of the density.
- **`main_matshow(dens_type)`**: Creates matrix-style plots to visualize the log-transformed density values in a heatmap format.
- **`main_contour(dens_type)`**: Produces contour plots that map the electron density across a defined grid.

Each function is designed to be used with different types of density data (e.g., total electron density or isolated electron density) specified through the `dens_type` parameter.

### Execution

To use the `make_plot.py` script, the user should call the script from the command line or within a Python environment. Each function can be executed individually based on the required visualization, handling the data extraction and plotting in a seamless manner. The script automates the creation of PDF files for each plot type, facilitating easy sharing and documentation of the results.

The script uses a structured approach to manage the complexities of data handling and visualization, making it accessible for users familiar with Python and data visualization techniques.
