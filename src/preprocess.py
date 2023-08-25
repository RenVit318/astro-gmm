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
    masked_data = hdul[0].data[:, mask].T  # Transpose to comply with PyGMMis (N, D) requirement
    return masked_data 


def reduce_dimensions(data, params):
    """Receives a HDUL and applies some dimensionality reduction algorithm to it.
    Returns an NxM numpy array where N is the number of data points and M the number of features
    """

    # First cut away any dimensions with low RMS
    rms_threshold = float(params['rms_threshold'])
    if rms_threshold > 0:
        rms_of_dim = np.sqrt(np.mean(data**2, axis=0))
        rms_mask = rms_of_dim > (rms_threshold * float(params['rms']))
        data = data[:, rms_mask]

    # Then apply other dimension reduction method (if any)
    method = params['reduce_method']

    # Could update to match-case but requires Python >3.10
    if method == 'none':
        return data

    else:
        raise NotImplementedError(f"Unknown Dim Reduction Method: {params['reduce_method']}. Please check config file")


def normalize(data, params):
    """Receives a NxM ndarray and applies some normalization method to it
    """
    method = params['norm_method']

    # Could update to match-case but requires Python >3.10
    if method == 'none':
        return data

    elif method == 'mean': # subtract mean from data
        return data - np.mean(data, axis=0)

    elif method == 'min-max':
        normed_data = data
        for i in range(len(data)):  # Normalize each spectrum separately between 0 and 1
            spec = data[i, :]
            normed_data[i, :] = (spec - np.min(spec)) / (np.max(spec) - np.min(spec))
        return normed_data

    else:
        raise NotImplementedError(f"Unknown Normalization Method: {params['norm_method']}. Please check config file")



