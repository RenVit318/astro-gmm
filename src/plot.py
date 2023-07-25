#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Visualize the PyGMMis results following style of Tiwari+23
"""

import matplotlib.pyplot as plt
import numpy as np

def set_styles():
    """Matches the plotting styles to those used in Tiwari+23"""
    import matplotlib as mpl
    mpl.pyplot.style.use('default')
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['lines.linewidth'] = 1.5
    mpl.rcParams['font.size'] = 14


def plot_weights_map(gmm, dmap, component_idxs, params):
    """"""
    # Set colormaps
    if np.nanmax(dmap) < 10:
        cmap = plt.cm.get_cmap('tab10')
        vals = np.arange(np.nanmax(dmap)+1)/10 # Set 'ticks' on the colorbar which runs from [0, 1]
        colors = [cmap(val) for val in vals]
    else: # Currently only supported up to 20 separate components
        cmap = plt.cm.get_cmap('tab20b')
        vals = np.arange(np.nanmax(dmap)+1)/20 # Set 'ticks' on the colorbar which runs from [0, 1]
        colors = [cmap(val) for val in vals]

    fig, ax = plt.subplots(1,1,figsize=(10, 6), tight_layout=True)
    ax.bar(np.arange(int(np.nanmax(dmap))+1)+1, gmm.amp[component_idxs], color=colors)
    
    ax.set_xticks(np.arange(int(np.nanmax(dmap)), dtype=int)+1)
    ax.set_xlabel('Component Number')
    ax.set_ylabel(r'Weight $\alpha_k$')
    plt.savefig(f"{params['results_path']}{params['source_name']}_{params['save_txt']}_weightmap.png", bbox_inches='tight')
 

def plot_domain_map(hdul, dmap, params):
    """"""
    from astropy.wcs import WCS

    # Set colormaps
    if np.nanmax(dmap) < 10:
        cmap_name = 'tab10'
        vmax = 9
    else: # Currently only supported up to 20 separate components
        cmap_name = 'tab20'
        vmax = 19

    fig = plt.figure(figsize=(10,8), tight_layout=True)
    ax = fig.add_subplot(projection=WCS(hdul[0].header)[0])
    ax.imshow(dmap, cmap=cmap_name, vmin=0, vmax=vmax, origin='lower')
    plt.savefig(f"{params['results_path']}{params['source_name']}_{params['save_txt']}_domainmap.png", bbox_inches='tight')


def plot_average_spectra(gmm, dmap, hdul, reduced_data, params):
    """"""    
    import astrokit
    from astropy.io import fits

    # Set colormaps
    if np.nanmax(dmap) < 10:
        cmap = plt.cm.get_cmap('tab10')
        vals = np.arange(np.nanmax(dmap)+1)/10 # Set 'ticks' on the colorbar which runs from [0, 1]
        colors = [cmap(val) for val in vals]          
    else: # Currently only supported up to 20 separate components
        cmap = plt.cm.get_cmap('tab20b')
        vals = np.arange(np.nanmax(dmap)+1)/20 # Set 'ticks' on the colorbar which runs from [0, 1]
        colors = [cmap(val) for val in vals]

    # astrokit can calculate average spectra. But only works with HDULs
    dmap_hdu = fits.PrimaryHDU(dmap)
    dmap_hdul = fits.HDUList([dmap_hdu])
    
    avg_spect_mean, avg_spect_std = astrokit.cluster_average_spectra(hdul, dmap_hdul)
    vel = astrokit.get_axis(3, hdul)/1e3 # Required to convert m/s -> km/s

    fig, ax = plt.subplots(1,1,figsize=(10, 6), tight_layout=True)
    for i in range(avg_spect_mean.shape[0]):
        ax.step(vel, avg_spect_mean[i], label=i+1, c=colors[i])
    ax.axhline(y=0, c='black', ls='--', alpha=0.7)

    ax.set_xlim(float(params['vel_min']), float(params['vel_max']))
    ax.set_xlabel(r'V$_{\rm LSR}$ (km/s)')
    ax.set_ylabel(r'$T_MB$ (K)')
    
    plt.savefig(f"{params['results_path']}{params['source_name']}_{params['save_txt']}_avg_spectra.png", bbox_inches='tight')





















