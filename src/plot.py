#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Visualize the PyGMMis results following style of Tiwari+23
"""

import matplotlib.pyplot as plt

def set_styles():
    """Matches the plotting styles to those used in Tiwari+23"""
    import matplotlib as mpl
    mpl.pyplot.style.use('default')
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['lines.linewidth'] = 1.5
    mpl.rcParams['font.size'] = 14

def plot_domain_map(dmap, params):
    plt.imshow(dmap, origin='lower')
    plt.savefig(f"{params['source_name']}_domainmap.png", bbox_inches='tight')

def plot_average_spectra():
    pass

def plot_weights_map():
    pass
