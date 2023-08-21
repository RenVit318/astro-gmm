This file provides a brief description of each parameter included in the params file included in this example directory

hdul_name: Name of the input cube
data_path: Path to the input cube relative to directory from which the script is run
results_path: Path to the directory where results can be saved relative to directory from which the script is run.

source_name: Name of the source in consideration. Used for automatic titles and file save names
rms: The RMS noise of the provided data cube given in data units (assumed to be Kelvin)

vel_min: Minimum velocity/frequency of the window provided to the algorithm. This is assumed to be in km/s for a data cube
         given in m/s, i.e. a multiplicative factor of 1e3 is applied behind the screen by astrokit.
vel_max: See vel_min, but the upper/maximum of the velocity window

rms_threshold: Potential RMS threshold to apply to data before continuing to further dimension reduction / normalization.
               It works by computing the RMS of all spatial pixels in a single channel. Any channels with RMS below the
               given threshold are thrown out.

reduce_method: Indicates which method to be used for the further reduction of the amount of dimensions in the data.
               Currently implemented methods are:
                - 'none': No further reduction of dimensions

norm_method: Method used for the normalization of the data. Currently implemented methods are:
                - 'none': No normalization applied to the data

covar_method: Shape of the covariance matrix provided to the GMM (as in PyGMMis code). Currently implemented methods are
                - 'diag': Makes the identity matrix with 'rms' on the diagonal

num_clusters: The number of clusters provided to the GMM. Referred to as n_input in the paper

w: The value of the covariance regularization. Can be either given as a float, or as a multiplicative factor of the rms
   which is written as e.g. 1rms or 3rms for 1 x rms and 3 x rms respectively

cutoff: As in PyGMMis. Indicates how far a point can be removed from the center of any cluster before its likelihood
        of belonging to that cluster is set to NaN. This has little effect on the results. We recommend leaving this at
        3 and increasing it only (to another integer) if there are pixels in the cube that remain unassigned.

save_txt: The base text used for the specific run of our recipe. Additional information such as 'domain_map' is attached
          behind this. If set to 'none', it is generated automatically based on 'source_name', n_input and the pre-
          processing parameters.

remove_comps: Which (if any) components to remove from the fitted GMM. Recommended to only be used if the GMM has already
              been fitted previously.

save_gmm: Save the weights, means and covariances of all GMM components combined with a dictionary containing 'params'
          as a .npy file
save_dmap: Save the domainmap as a .npy file
save_figs: Create and save a weight map, domainmap and average spectra plot as in the paper as .png files

Below are parameters specifically for the determination of the optimal n_input
min_n: Number of components to start the n_input vs. n_output search
max_n: Number of components to stop the n_input vs. n_output search, including the provided value
stepsize_n: Size of steps from one n_input to the next
num_iterations: Number of times to repeat the fitting of the GMM on one specific n_input