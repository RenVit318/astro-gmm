#!/usr/bin/env python
# -*- coding: utf-8 -*-

def full_run(hdul, fit_params, plot_params):
    """Full iteration of the GMM algorithm from a data cube to a fitted model with corresponding plots.
    Hyperparameter settings are set through the fit_params dictionary
    INPUTS:
       - hdul: FITS file of the wanted cube. The data should be accessible as hdul[0].data
       - fit_params: Should contain all keyword arguments needed for the data preprocessing and fitting procedures
                     Any keyword arguments not provided are assumed 'None' or 0 to assist argument contamination discovery
       - plot_params: Describes which plots should be made, can also contain kwargs given to matplotlib
    """
    return
    # Following the steps of the paper
    # 1. Cut out dimensions outside of velocity range
    chop_hdul = hdul  # TODO: DO SOMETHING HERE

    # 2. Apply dimensionality reduction and normalization
    # This takes a hdul object as input and returns a numpy array
    reduced_data = reduce_dimensions(chop_hdul, fit_params)
    normed_data = normalize(reduced_data, fit_params)

    # 3. Fit the GMM model
    # This returns a PyGMMis object containing all weights, means and covariances
    gmm = fit_model(normed_data, fit_params)

    # 4. Do plotting things

