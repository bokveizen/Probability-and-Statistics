from scipy.stats import t
import numpy as np

mu0 = 13
alpha = 0.05
mean = 12  # x bar
s = 4  # sample std
n = 50  # sample size

df = n - 1
t_stat = np.sqrt(n) * (mean - mu0) / s

H0_type = 0
if H0_type:
    # H_0: \mu <= \mu_0 versus H_A: \mu > \mu_0
    p = t.sf(t_stat, df=df)

else:
    # H_0: \mu >= \mu_0 versus H_A: \mu < \mu_0
    p = t.cdf(t_stat, df=df)
