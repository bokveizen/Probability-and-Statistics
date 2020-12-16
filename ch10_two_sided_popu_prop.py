from scipy.stats import norm
import numpy as np

alpha = 0.05
n = 23
x = 14
p_hat = x / n
# hypo
p0 = 0.5

se = np.sqrt(p_hat * (1 - p_hat) / n)
z_crit = norm.isf(alpha / 2)
z_interval = (p_hat - z_crit * se, p_hat + z_crit * se)

se0 = np.sqrt(p0 * (1 - p0) / n)
z_stat = (p_hat - p0) / se0
# improvement
if x - n * p0 > 0.5:
    z_stat = (x - n * p0 - 0.5) / (n * se0)
elif x - n * p0 < -0.5:
    z_stat = (x - n * p0 + 0.5) / (n * se0)
# H0: p = p0 is accepted if |z_stat| <= z_crit
p = 2 * norm.cdf(-np.abs(z_stat))

# sample size calc
L = 2 * z_crit * se
L0 = 2  # required confidence interval length
p_star = 0.5
n = 4 * np.square(z_crit / L0) * p_star * (1 - p_star)
# when p_star is 0.5, n = np.square(z_crit / L0)
