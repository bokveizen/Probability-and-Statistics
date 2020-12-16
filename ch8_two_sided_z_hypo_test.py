from scipy.stats import norm
import numpy as np

# H_0: \mu = \mu_0 versus H_A: \mu \neq \mu_0
mu0 = 50
alpha = 0.1
mean = 49.999  # x bar
sigma = 0.134  # "known" std
n = 60  # sample size

df = n - 1

z_stat = np.sqrt(n) * (mean - mu0) / sigma
p = 2 * norm.cdf(-np.abs(z_stat))
