from scipy.stats import norm
import numpy as np

alpha = 0.01
# population A
n = 24
mean_x = 9.005
sigma_x = 3.438  # "known" std
# population B
m = 34
mean_y = 11.864
sigma_y = 3.305  # "known" std

diff = mean_x - mean_y
se = np.sqrt(np.square(sigma_x) / n + np.square(sigma_y) / m)
z_crit = norm.isf(alpha)
z_interval_upper_bd = diff + z_crit * se
z_interval_lower_bd = diff - z_crit * se

delta = 0
z_stat = (diff - delta) / se

H0_type = 0
if H0_type:  # H0: diff <= delta
    p = 1 - norm.cdf(z_stat)
    # H0 is accepted if z_stat <= z_crit
else:  # H0: diff >= delta
    p = norm.cdf(z_stat)
    # H0 is accepted if z_stat >= -z_crit


