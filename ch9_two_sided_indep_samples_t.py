from scipy.stats import t
import numpy as np

alpha = 0.05
# population A
# A = np.array([34,27,29,30,29,32,30,35,28,26])
n = 8
mean_x = 5.9
s_x = 1.9
# population B
# B = np.array([25,30,27,22,36,26,23,31])
m = 19
mean_y = 9.4
s_y = 3.2

diff = mean_x - mean_y
se = np.sqrt(np.square(s_x) / n + np.square(s_y) / m)
v = int(np.power(se, 4) / (np.power(s_x, 4) / (np.square(n) * (n - 1)) + np.power(s_y, 4) / (np.square(m) * (m - 1))))
# v = min(m, n) - 1
t_crit = t.isf(alpha / 2, v)
t_interval = (diff - t_crit * se, diff + t_crit * se)

delta = 0
t_stat = (diff - delta) / se
p = 2 * t.sf(np.abs(t_stat), df=v)
# H0: diff = delta is accepted if |t_stat| <= t_crit

# sample size calculation
L = 2 * t_crit * se
L0 = 2  # desired confidence interval length
# if n = m, minimal n0 = m0 is
n0 = 4 * np.square(t_crit) * (np.square(s_x) + np.square(s_y)) / np.square(L0)
