from scipy.stats import f
import numpy as np
from statsmodels.stats.libqsturng import psturng, qsturng

alpha = 0.05
mean_list = [25.125, 29.11, 1362 / 55]
mean_list = np.array(mean_list, dtype=float)
mean_total = 865 / 33
# n_list = [len(x) for x in x_list]
n_list = [12, 10, 11]
n_T = sum(n_list)
k = len(mean_list)
sum_square = 22829.14

SST = sum_square - n_T * np.square(mean_total)
SSTr = sum(n_list[i] * np.square(mean_list[i]) for i in range(k)) - n_T * np.square(mean_total)
SSE = SST - SSTr

# The mean squares for treatments
MSTr = SSTr / (k - 1)
# The mean square error
MSE = SSE / (n_T - k)
F_stat = MSTr / MSE
p = f.sf(F_stat, dfn=k - 1, dfd=n_T - k)
# H0: all means are equal

# q (alpha, k, v)
s = np.sqrt(MSE)
q = qsturng(p=1 - alpha, r=k, v=n_T - k)
for i1 in range(k - 1):
    for i2 in range(i1 + 1, k):
        diff = mean_list[i1] - mean_list[i2]
        lower_bd = diff - s * q * np.sqrt(0.5 / n_list[i1] + 0.5 / n_list[i2])
        upper_bd = diff + s * q * np.sqrt(0.5 / n_list[i1] + 0.5 / n_list[i2])
        print('({}, {}): ({}, {})'.format(i1+1, i2+1, lower_bd, upper_bd))

# when all ni are equal (= n), L = 2 * s * q * np.sqrt(1 / n)
# required length
L0 = 2
n0 = 4 * np.square(s * q / L0)