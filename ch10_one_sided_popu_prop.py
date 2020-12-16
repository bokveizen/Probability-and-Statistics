from scipy.stats import norm
import numpy as np

alpha = 0.01
n = 500000
x = 372
p_hat = x / n
# hypo
p0 = 0.001
H0_type = 1

se = np.sqrt(p_hat * (1 - p_hat) / n)
z_crit = norm.isf(alpha)
z_interval_upper_bd = p_hat + z_crit * se
z_interval_lower_bd = p_hat - z_crit * se

se0 = np.sqrt(p0 * (1 - p0) / n)
if H0_type:  # H0: p >= p0
    z_stat = (x - n * p0 + 0.5) / (n * se0)
    p = norm.cdf(z_stat)
    # H0 is accepted if z_stat >= -z_crit
else:  # H0: p <= p0
    z_stat = (x - n * p0 - 0.5) / (n * se0)
    p = 1 - norm.cdf(z_stat)
    # H0 is accepted if z_stat <= z_crit


