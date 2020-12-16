from scipy.stats import t
import numpy as np

alpha = 0.05
# population A
n = 15
mean_x = 47.47
s_x = 11.40
# population B
m = 15
mean_y = 51.20
s_y = 10.09
# hypo
delta = 0
H0_type = 0

diff = mean_x - mean_y
se = np.sqrt(np.square(s_x) / n + np.square(s_y) / m)
v = int(np.power(se, 4) / (np.power(s_x, 4) / (np.square(n) * (n - 1)) + np.power(s_y, 4) / (np.square(m) * (m - 1))))
# v = min(m, n) - 1
t_crit = t.isf(alpha, v)
t_interval_upper_bd = diff + t_crit * se
t_interval_lower_bd = diff - t_crit * se

t_stat = (diff - delta) / se
if H0_type:  # H0: diff <= delta
    p = t.sf(t_stat, df=v)
    # H0 is accepted if t_stat <= t_crit
else:  # H0: diff >= delta
    p = t.cdf(t_stat, df=v)
    # H0 is accepted if t_stat >= -t_crit
