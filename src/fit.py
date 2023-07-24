#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Call the PyGMMis model and fit it to the data
 Use the fitted model to make a domain map
"""

import numpy as np
import pygmmis


def make_covar(num_features, params):
    """Make the covariance matrix depending on rms and given type"""
    # update to match-case?
    method = params['covar_method']

    if method == 'diag':
        return np.eye(num_features) * (params['rms']**2)


def fit_model(data, params):
    """"""
    # Set up the covariance matrix and the GMM object
    num_features = data.shape[1]  # MIGHT CHANGE!!
    covar = make_covar(num_features, params)
    gmm = pygmmis(K=params['num_clusters'], D=num_features)

    # Actually fit the model using the adjusted EM algorithm (Melchior & Goulding 2018)
    logL, U = pygmmis.fit(gmm, data, covar=covar, w=params['w'], cutoff=params['cutoff'])

    return gmm


def make_domain_map():
    """"""
    # Copy code from Notebook here
    pass
    
    if params['save_dmap']:
        np.save(RPATH+'_'+params['source_name']+'_'+params['save_txt']+'_dmap.npy')
