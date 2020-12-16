from scipy.stats import norm
import numpy as np

alpha = 0.1
mean = 49.999  # x bar
sigma = 0.134  # "known" std
n = 60  # sample size

z_stat = norm.isf(alpha)
z_interval_upper_bd = mean + z_stat * sigma / np.sqrt(n)
z_interval_lower_bd = mean - z_stat * sigma / np.sqrt(n)



