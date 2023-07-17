#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Call the PyGMMis model and fit it to the data
 Use the fitted model to make a domain map
"""

import numpy as np
import pygmmis


def make_covar(num_features, fit_params):
    """Make the covariance matrix depending on rms and given type"""
    # update to match-case?
    method = fit_params['covar_method']

    if method == 'diag':
        return np.eye(num_features) * (fit_params['rms']**2)


def fit_model(data, fit_params):
    """"""
    # Set up the covariance matrix and the GMM object
    num_features = data.shape[1]  # MIGHT CHANGE!!
    covar = make_covar(num_features, fit_params)
    gmm = pygmmis(K=fit_params['num_clusters'], D=num_features)

    # Actually fit the model using the adjusted EM algorithm (Melchior & Goulding 2018)
    logL, U = pygmmis.fit(gmm, data, covar=covar, w=fit_params['w'], cutoff=fit_params['cutoff'])

    return gmm


def make_domain_map():
    """"""
    # Copy code from Notebook here
    pass
    
    if fit_params['save_dmap']:
        np.save(RPATH+'_'+fit_params['source_name']+'_'+fit_params['save_txt']+'_dmap.npy')
