#!/usr/bin/env python
# -*- coding: utf-8 -*-

from preprocess import reduce_dimensions, normalize
from fit import fit_model

import astrokit # https://github.com/skabanovic/astrokit
print(astrokit)
print(specube.chop_cube)

def full_run(hdul, fit_params, plot_params):
    """Full iteration of the GMM algorithm from a data cube to a fitted model with corresponding plots.
    Hyperparameter settings are set through the fit_params dictionary
    INPUTS:
       - hdul: FITS file of the wanted cube. The data should be accessible as hdul[0].data
       - fit_params: Should contain all keyword arguments needed for the data preprocessing and fitting procedures
                     Any keyword arguments not provided are assumed 'None' or 0 to assist argument contamination discovery
       - plot_params: Describes which plots should be made, can also contain kwargs given to matplotlib
    """
    # Check if additional information was given for file saving. If not make it based on parameters
    print(f"Starting full GMMis run for {fit_params['source_name']}")
    save_check(fit_params, plot_params)

    # Following the steps of the paper
    # 1. Cut out dimensions outside of velocity range
    chop_hdul = astrokit.prism.specube.chop_cube(fit_params['vel_min'], fit_params['vel_max'], hdul)  

    # 2. Apply dimensionality reduction and normalization
    # This takes a hdul object as input and returns a numpy array
    reduced_data = reduce_dimensions(chop_hdul, fit_params)
    normed_data = normalize(reduced_data, fit_params)

    # 3. Fit the GMM model
    # This returns a PyGMMis object containing all weights, means and covariances
    gmm = fit_model(normed_data, fit_params)

    # 4. Do plotting things
    dmap = make_domain_map(gmm, chop_hdul, fit_params)

    plot_domain_map(dmap, plot_params)
    #plot_average_spectra(gmm, 



def save_check(fit_params, plot_params):
    """Checks if save file information is provided and prints it. If it is not provided, a savename is created
    based on the input parameters."""
    
    if fit_params['save_txt'] == 'none':
        fit_params['save_txt'] = f"{fit_params['norm_method']}-{fit_params['norm_thresh']}_{fit_params['vel_min']}-{fit_params['vel_max']}"


    print(f"Saving Files with text: {fit_params['source_name']}_{fit_params['save_txt']}")
    print(f" GMM\t{fit_params['save_gmm']}\n dmap\t{fit_params['save_dmap']}\n figs\t{plot_params['save_figs']}")


    
        



