from scipy.stats import t
import numpy as np

alpha = 0.05
mean = 12.0  # x bar
s = 4.0  # sample std
n = 50  # sample size

df = n - 1
# x bar +/- t_{\alpha, n-1} s / \sqrt{n}
t_stat = t.isf(alpha, df)
t_interval_upper_bd = mean + t_stat * s / np.sqrt(n)
t_interval_lower_bd = mean - t_stat * s / np.sqrt(n)


