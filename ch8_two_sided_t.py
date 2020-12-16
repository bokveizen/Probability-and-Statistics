from scipy.stats import t
import numpy as np

alpha = 0.1
mean = 49.999  # x bar
s = 0.134  # sample std
n = 60  # sample size

df = n - 1
# \mu \in x bar \pm t_{\alpha/2, n-1} s / \sqrt{n}
t_stat = t.isf(alpha / 2, df)
t_interval = (mean - t_stat * s / np.sqrt(n), mean + t_stat * s / np.sqrt(n))
L = 2 * t_stat * s / np.sqrt(n)  # the length of the confidence interval
# L0 is required
L0 = 2
# minimum sample size for L0
n0 = 4 * np.square(t_stat * s / L0)

