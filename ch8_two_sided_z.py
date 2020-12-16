from scipy.stats import norm
import numpy as np

alpha = 0.1
mean = 49.999  # x bar
sigma = 0.134  # "known" std
n = 60  # sample size

z_stat = norm.isf(alpha / 2)
z_interval = (mean - z_stat * sigma / np.sqrt(n), mean + z_stat * sigma / np.sqrt(n))
L = 2 * z_stat * sigma / np.sqrt(n)  # the length of the confidence interval
# L0 is required
L0 = 2
# minimum sample size for L0
n0 = 4 * np.square(z_stat * sigma / L0)


