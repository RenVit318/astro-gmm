#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Apply data normalization and dimension reduction to a data cube
 and prepare it to be fed into the PyGMMis
 The functions used here are adaptations based on functions in astrokit by Dr. S. Kabanovic
"""

import numpy as np


def remove_nans(hdul):
    """Remove all lines of sight where any channel along it has a NaN value.
    This assumes that axis the velocity/frequency axis"""
    mask = np.isfinite(hdul[0].data).all(axis=0)
    masked_data = hdul[0].data[:, mask].T # Transpose to comply with PyGMMis (N, D) requirement
    return masked_data 

def reduce_dimensions(data, params):
    """Receives a HDUL and applies some dimensionality reduction algorithm to it.
    Returns an NxM numpy array where N is the number of data points and M the number of features
    """

    method = params['reduce_method']

    # Could update to match-case but requires Python >3.10
    if method == 'none':
        return data  
    elif method == 'rms_thresh':
        return



def normalize(data, params):
    """Receives a NxM ndarray and applies some normalization method to it
    """
    method = params['norm_method']

    # Could update to match-case but requires Python >3.10
    if method == 'none':
        return data



