# BCI Competition IV 2a Dataset for Python/NumPy

This repository provides the BCI Competition 2008 Dataset IV 2a in a format optimized for Python and NumPy. The dataset is focused on motor imagery and has been converted from the original GDF files, with the signals and events extracted for ease of use.

## Getting Started

To get started with this dataset, we recommend reading the original paper, which details the data acquisition process. The dataset includes data for four motor imagery tasks: imagining the movement of the left hand (class 1), the right hand (class 2), both feet (class 3), and the tongue (class 4).

The dataset is structured as follows:

- **9 subjects**
- **288 trials** per subject, with **48 trials** for each of the four classes

Each event in the dataset is coded according to the table provided in the original paper. For a complete understanding of the dataset, please refer to the original paper, available [here](http://bbci.de/competition/iv/desc_2a.pdf).

### Data Files

The data is provided in `.npz` format, which can be loaded using `numpy.load()`. Each file contains the following keys:

-   `s`: The raw EEG data, stored in a NumPy array.
-   `etyp`: The type of each event.
-   `epos`: The position of each event.
-   `edur`: The duration of each event.

### Data Loader

A `MotorImageryDataset` class is available in `data_loader.py` to simplify loading and preprocessing the data.

#### Installation

To use the data loader, you need to install the following dependencies:

```bash
pip install numpy
```

#### Usage

Here is an example of how to use the `MotorImageryDataset` class:

```python
from data_loader import MotorImageryDataset

# Load the data for subject 1's training session
dataset = MotorImageryDataset(data_path='.', subject=1, session='T')

# Get all trials and corresponding classes
trials, classes = dataset.get_trials()

# Get trials and classes for specific channels (e.g., C3, Cz, C4)
trials, classes = dataset.get_trials(channels=[7, 9, 11])
```

## Example: Visualizing Trials

This example demonstrates how to extract and visualize trials from one subject. The `try-except` block is used to handle trials that may have been rejected.

```python
from data_loader import MotorImageryDataset
from matplotlib import pyplot as plt

# Load the dataset for subject 1
datasetA1 = MotorImageryDataset('.', subject=1, session='T')

# Get trials from channels C3, Cz, and C4
trials, classes = datasetA1.get_trials_from_channels([7, 9, 11])

# Plot the trials
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.imshow(trials[0])
plt.title('C3', fontsize=16)

plt.subplot(3, 1, 2)
plt.imshow(trials[1])
plt.title('Cz', fontsize=16)

plt.subplot(3, 1, 3)
plt.imshow(trials[2])
plt.title('C4', fontsize=16)

plt.tight_layout()
plt.show()
```

## References

-   Brunner, C., Leeb, R., Müller-Putz, G., Schlögl, A., & Pfurtscheller, G. (2008). *BCI Competition 2008 – Graz data set A*. Institute for Knowledge Discovery, Graz University of Technology. Retrieved from [http://bbci.de/competition/iv/desc_2a.pdf](http://bbci.de/competition/iv/desc_2a.pdf)

## Contributing

Contributions are welcome! If you would like to contribute, please open an issue to get started.
