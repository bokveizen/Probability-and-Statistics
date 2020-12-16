from scipy.stats import f
import numpy as np
from statsmodels.stats.libqsturng import psturng, qsturng

alpha = 0.05
x_list = [
    [11, 30, 36, 23],
    [8, 31, 25, 36],
    [13, 28, 28, 31]
]
mean_list = np.mean(x_list, axis=1)
n_list = [len(x) for x in x_list]
n_T = sum(n_list)
k = len(mean_list)
# mean_total = np.dot(mean_list, n_list) / n_T  # x bar ..
mean_total = np.sum(x_list) / n_T
# The sum of squares for treatments SSTr is a measure of the variability between the factor levels.
SSTr = sum(n_list[i] * np.square(mean_list[i] - mean_total) for i in range(k))
# The sum of squares for error SSE is a measure of the variability within the factor levels.
SSE = 0
for i in range(k):
    for j in range(n_list[i]):
        SSE += np.square(x_list[i][j] - mean_list[i])
# The total sum of squares
SST = SSTr + SSE

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
        print('({}, {}): ({}, {})'.format(i1 + 1, i2 + 1, lower_bd, upper_bd))
        # confidence interval length
        L = 2 * s * q * np.sqrt(0.5 / n_list[i1] + 0.5 / n_list[i2])

# when all ni are equal (= n), L = 2 * s * q * np.sqrt(1 / n)
# required length
L0 = 2
n0 = 4 * np.square(s * q / L0)
