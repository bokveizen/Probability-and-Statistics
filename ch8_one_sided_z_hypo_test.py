from scipy.stats import norm
import numpy as np


mu0 = 58
alpha = 0.05
mean = 60  # x bar
sigma = 33  # "known" std
n = 121  # sample size

df = n - 1

z_stat = np.sqrt(n) * (mean - mu0) / sigma

H0_type = 1
if H0_type:
    # H_0: \mu <= \mu_0 versus H_A: \mu > \mu_0
    p = 1 - norm.cdf(z_stat)

else:
    # H_0: \mu >= \mu_0 versus H_A: \mu < \mu_0
    p = norm.cdf(z_stat)


