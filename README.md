# Astro-GMM

Repository implementing the PyGMMis (Melchior & Goudling 2018) method to astronomical data cubes of velocity resolved line observations. This implementation is described extensively in Tiwari et al. (subm. to ApJ).

An example is included in /example/ containing the SOFIA data of RCW120 used in Tiwari et al. (subm. to ApJ) along with example scripts describing the full implementation of our code. The majority of parameter tweaking can be performed within 'rcw120-params.txt' which is continuously called during the procedure. 

--

## User Guide

### Installation

1. Before starting any scripts provided here it is required one installs astrokit by Dr. S. Kabanovic which can be downloaded and then installed at https://github.com/skabanovic/astrokit/
2. We recommend downloading the scripts from /src/ into a local directory instead of importing or pip installing this repository

### Preparation

Almost all functions of astroGMM take various parameters as inputs which are assumed to be handled from a single dictionary. In /example/ all these named parameters are introduced in 'params_readme.txt' and example parameters as in Tiwari et al. (subm. to ApJ) for RCW120 are given in 'rcw120-params.txt'. When using astroGMM one should carefully read through the parameters readme and adjust values accordingly. The most important parameters are

- 'hdul_name', 'data_path': These should point to the .fits file relative to the directory from which the script is run
- 'results_path': Should point towards the directory where fit results and figures will be saved
- 'rms': RMS noise of the cube
- 'vel_min' and 'vel_max': Should encompass the window of emission in km/s
- 'save_txt': Either provide a fitting savename, or can be set to 'none' for dynamic naming.
- 'num_clusters': Can optimally be determined using the n_input vs n_output method introduced in Tiwari et al. (subm. to ApJ) using the same parameter file and the example script provided as 'ninput-rcw120.py'. Do this only after you are satisfied with all other parameters.

For the rest we recommend reading Tiwari et al. (subm. to ApJ) and the parameter README.

### Fitting

The complete GMM fitting procedure takes the following steps

1. It starts in 'gmm-rcw120.py' where it reads in the parameter file as a dictionary and the cube as a fits file.
2. It calls the function full_run() in main.py
   1. The wanted data pre-processing steps (located in preprocess.py) are applied:
      1. Any channels with RMS below rms_threshold are discarded
      2. (Optionally) additional dimensions are discarded
      3. (Optionally) the data is normalized
   2. The processed data is passed to fit_model() in fit.py
      1. The covariance matrix is set up using 'covar_method' and the provided rms
      2. The PyGMMis function is called to create a GMMis object and fit it to the processed data
   3. A domain map is made by assigning each pixel to the cluster to which it has the highest probability of belonging. After this the cluster number are reorder such that they form an ordered list as 0, 1, .. K-1 with K the number of clusters in the final domain map.
   4. (Optionally) figures are made and saved in the results path.

---

## Script Structure

 - main.py
    - Master script containg 'full_run' which runs through the complete procedure from raw data and parameter file to a fitted GMM including (if wanted) domain map and plots.

 - fit.py
    - Functions calling the PyGMMis code by Melchior & Goulding. Includes domainmap creation code and save/load functionality for the GMM.

 - preprocess.py
    - All normalization/dimensionality reduction steps to be performed on raw data to increase model performance. The function 'improve_nans' is required as it both removes NaN values (PyGMMis breaks if it encounters these) and reshapes the datacube into the correct form.

 - plot.py
    - Plotting code following the style from Tiwari et al. (subm. to ApJ), relatively straightforward.

