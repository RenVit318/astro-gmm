# Astro-GMM

Repository implementing the PyGMMis (Melchior & Goudling 2018) method to astronomical data cubes of velocity resolved line observations. This implementation was introduced and tested by Tiwari et al. (in prep).

An example is included in /example/ containing the SOFIA data of RCW120 used in the afor mentioned paper along with example scripts describing the full implementation of our code. The majority of parameter tweaking can be performed within 'rcw120-params.txt' which is continuously called during the procedure. 

---

## Script Structure

 - main.py
    - Master script containg 'full_run' which runs through the complete procedure from raw data and parameter file to a fitted GMM including (if wanted) domain map and plots.

 - fit.py
    - Functions calling the PyGMMis code by Melchior & Goulding. Includes domainmap creation code and save/load functionality for the GMM.

 - preprocess.py
    - All normalization/dimensionality reduction steps to be performed on raw data to increase model performance. The function 'improve_nans' is required as it both removes NaN values (PyGMMis breaks if it encounters these) and reshapes the datacube into the correct form.

 - plot.py
    - Plotting code following the style from our paper, relatively straightforward.

