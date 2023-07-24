#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Example script showing the application of astro-gmm to RCW 120
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
from fit import fit_model
from main import full_run

# External
from astropy.io import fits
import json


def main():
    hdul = fits.open('../example/rcw120-cii-20arcsec-0-5kms.fits')

    with open('../example/rcw120-params.txt') as f:
        fit_txt = f.read()
        params = json.loads(fit_txt)

    full_run(hdul, params)



if __name__ == '__main__':
    main()
