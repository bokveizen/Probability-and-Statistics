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
z_crit = norm.isf(alpha / 2)
z_interval = (diff - z_crit * se, diff + z_crit * se)

delta = 0
z_stat = (diff - delta) / se
p = 2 * norm.sf(np.abs(z_stat))
# H0: diff = delta is accepted if |t_stat| <= t_crit

