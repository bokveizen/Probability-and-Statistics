from scipy.stats import t
import numpy as np

alpha = 0.01
# population A
n = 24
mean_x = 9.005
s_x = 3.438
# population B
m = 34
mean_y = 11.864
s_y = 3.305
# equal var assumption
s_p = np.sqrt(((n - 1) * np.square(s_x) + (m - 1) * np.square(s_y)) / (n + m - 2))
# hypo
delta = 0
H0_type = 0


diff = mean_x - mean_y
se = s_p * np.sqrt(1 / n + 1 / m)
v = n + m - 2
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

