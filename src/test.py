#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Example script showing the application of astro-gmm to RCW 120
 TODO: MOVE THIS TO EXAMPLE. FIX RELATIVE IMPORT
"""

from fit import fit_model
from main import full_run

from astropy.io import fits
import json

def main():
    hdul = fits.open('../example/rcw120-cii-20arcsec-0-5kms.fits')

    with open('../example/rcw120-fitparams.txt') as f:
        fit_txt = f.read()
        fit_params = json.loads(fit_txt)

    with open('../example/rcw120-plotparams.txt') as f:
        plot_txt = f.read()
        plot_params = json.loads(plot_txt)

    full_run(hdul, fit_params, plot_params)



if __name__ == '__main__':
    main()