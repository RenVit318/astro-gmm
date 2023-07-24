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
        return np.eye(num_features) * (np.float64(params['rms'])**2)


def fit_model(data, params):
    """"""
    # Set up the covariance matrix and the GMM object
    num_features = data.shape[1]  # MIGHT CHANGE!!
    covar = make_covar(num_features, params)  
    print(covar)
    gmm = pygmmis.GMM(K=int(params['num_clusters']), D=num_features)
    print('fitting..')
    # Actually fit the model using the adjusted EM algorithm (Melchior & Goulding 2018)
    logL, U = pygmmis.fit(gmm, data, covar=covar, w=np.float64(params['w']), cutoff=np.float64(params['cutoff']))
    print('done')
    return gmm


def make_domain_map(gmm, normed_data, hdul, fit_params):
    """"""

    # Initialize empty map which we fill with the likeliest component for each pixel
    dim_ax1 = hdul[0].header['NAXIS1']  # X/RA
    dim_ax2 = hdul[0].header['NAXIS2']  # Y/Dec
    dmap = np.full((dim_ax2, dim_ax1), np.nan)

    # log-likelihood cube to see each P(x|k)
    ll_cube = np.full((gmm.K, dmap.shape[0], dmap.shape[1]), np.nan)

    # Consider only the pixels where all datapoints are not NaN
    map_pixels = np.where(np.isfinite(hdul[0].data).all(axis=0))

    # Slow because iterates through dim_ax1*dim_ax2*num_cluster calculations, but it works
    for i in range(normed_data.shape[0]):
        L = - np.inf
        pix_cluster = np.nan  # Set to NaN in case ll = NaN for all k
        for k in range(gmm.K):  # gmm.K = No. Components
            ll = gmm.logL_k(k, normed_data[i])  # Calculate the likelihood that the pixel originates from component k
            ll_cube[
                k, map_pixels[0][i], map_pixels[1][i]] = 10 ** ll  # watch out here for underflow, different method?
            if ll > L:  # Select biggest likelihood
                pix_cluster = k
                L = ll

            dmap[map_pixels[0][i], map_pixels[1][i]] = pix_cluster

    # Find out which components are actually used in the domain map, and store them for later indexing
    component_idxs = np.unique(dmap)
    component_idxs = component_idxs[~np.isnan(component_idxs)]  # Throuw out 'NaN'
    component_idxs = np.array(component_idxs, dtype=int)  # For indexing later

    # Shift indices down such that we have components 0,.. instead of 'random' numbers
    new_vals = np.arange(len(component_idxs))
    new_vals = new_vals[~np.isnan(new_vals)]

    for i in range(len(component_idxs)):
        dmap[dmap == component_idxs[i]] = new_vals[i]

    if fit_params['save_dmap']:
        np.save(fit_params['RPATH'] + '_' + fit_params['source_name'] + '_' + fit_params['save_txt'] + '_dmap.npy')

    return dmap, ll_cube

