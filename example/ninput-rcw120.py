#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Example script showing how to determine the optimal number of input clusters
"""

# Weird PATH things, should be a better way to fix this?
from pathlib import Path
import os
import sys
ex_dir = os.path.dirname(os.path.abspath(__file__))
git_dir = str(Path(ex_dir).parents[0])
src_dir = os.path.join(git_dir, 'src')
sys.path.append(src_dir)
###

# This module


# External
from astropy.io import fits
import json
import numpy as np


def main():
    with open('../example/rcw120-params.txt') as f:
        fit_txt = f.read()
        params = json.loads(fit_txt) # Only need a subset of the parameters

    hdul = fits.open(params['data_path']+params['hdul_name'])

    # Preproces the data (identical to full_run( ))
    # Following the steps of the paper
    # 1. Cut out dimensions outside of velocity range
    chop_hdul = astrokit.chop_cube(np.float64(params['vel_min']), 
                                   np.float64(params['vel_max']),
                                   hdul)  

    # 2. Apply dimensionality redution and normalization
    # This takes a hdul object as input and returns a numpy array
    masked_data = remove_nans(chop_hdul)
    reduced_data = reduce_dimensions(masked_data, params)
    normed_data = normalize(reduced_data, params)

    # n_input is taken from 'min_n' up to and including  'max_n' 
    n_input = np.arange(params['min_n'], params['max_n']+.1, params['stepsize_n'])
    n_output = np.zeros((len(n_input), params['num_iterations']), dtype=int)
    
    # Loop over the desired cluster numbers with N iterations
    params['remove_comps'] = "none" 
    for i, n in enumerate(n_input):
        params['num_clusters'] = n # only adjusted locally
        for j in range(params['num_iterations']):
            gmm = fit_model(normed_data, params) 
            dmap, _, _ = make_domain_map(gmm, hdul, normed_data, params)
            n_output[i][j] = np.nanmax(dmap) + 1        

    np.save(f"noutput_minn{params['min_n']}_maxn{parmas['max_n']}_step{params['stepsize_n']}.npy", n_output)
        

if __name__ == '__main__':
    main()
