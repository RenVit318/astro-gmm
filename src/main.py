#!/usr/bin/env python
# -*- coding: utf-8 -*-

from preprocess import remove_nans, reduce_dimensions, normalize
from fit import fit_model

import astrokit # https://github.com/skabanovic/astrokit
import numpy as np


def full_run(hdul, params):
    """Full iteration of the GMM algorithm from a data cube to a fitted model with corresponding plots.
    Hyperparameter settings are set through the params dictionary
    INPUTS:
       - hdul: FITS file of the wanted cube. The data should be accessible as hdul[0].data
       - params: Should contain all keyword arguments needed for the data preprocessing and fitting procedures
                     Any keyword arguments not provided are assumed 'None' or 0 to assist argument contamination discovery
    """
    # Check if additional information was given for file saving. If not make it based on parameters
    print(f"Starting full GMMis run for {params['source_name']}")

    # Following the steps of the paper
    # 1. Cut out dimensions outside of velocity range
    chop_hdul = astrokit.chop_cube(np.float64(params['vel_min']), 
                                   np.float64(params['vel_max']),
                                   hdul)  

    # 2. Apply dimensionality redution and normalization
    # This takes a hdul object as input and returns a numpy array
    print(chop_hdul[0].data.shape)
    masked_data = remove_nans(chop_hdul)
    print(masked_data.shape)
    input() 
    reduced_data = reduce_dimensions(masked_data, params)
    normed_data = normalize(reduced_data, params)
    input('normalized data. PRESS ENTER')
    # 3. Fit the GMM model
    # This returns a PyGMMis object containing all weights, means and covariances
    input('Fit Model?')
    gmm = fit_model(normed_data, params)

    # 4. Do plotting things
    dmap = make_domain_map(gmm, chop_hdul, params)

    plot_domain_map(dmap, params)
    #plot_average_spectra(gmm, 



def save_check(params):
    """Checks if save file information is provided and prints it. If it is not provided, a savename is created
    based on the input parameters."""
    
    if params['save_txt'] == 'none':
        params['save_txt'] = f"{params['norm_method']}-{params['norm_thresh']}_{params['vel_min']}-{params['vel_max']}"


    print(f"Saving Files with text: {params['source_name']}_{params['save_txt']}")
    print(f" GMM\t{params['save_gmm']}\n dmap\t{params['save_dmap']}\n figs\t{params['save_figs']}")


    
        



