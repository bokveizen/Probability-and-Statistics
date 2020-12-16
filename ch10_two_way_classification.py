from scipy.stats import chi2
import numpy as np

alpha = 0.01
freq_list = [
    [11, 30, 36, 23],
    [8, 31, 25, 36],
    [13, 28, 28, 31]
]
r = len(freq_list)
c = len(freq_list[0])
n = np.sum(freq_list)
# hypo, H0: independence between two categorizations
expected_freq_list = np.zeros_like(freq_list, dtype=float)
for i in range(r):
    for j in range(c):
        expected_freq_list[i][j] = np.sum(freq_list, axis=1)[i] * np.sum(freq_list, axis=0)[j] / n
v = (r - 1) * (c - 1)
chi2_crit = chi2.isf(alpha, df=v)
# Pearson chi-square statistic
X_square = 0
for i in range(r):
    for j in range(c):
        x_ij = freq_list[i][j]
        e_ij = expected_freq_list[i][j]
        X_square += np.square(x_ij - e_ij) / e_ij
# likelihood ratio chi-square statistic
G_square = 0
for i in range(r):
    for j in range(c):
        x_ij = freq_list[i][j]
        e_ij = expected_freq_list[i][j]
        G_square += 2 * x_ij * np.log(x_ij / e_ij)
p_X = chi2.sf(X_square, df=v)
p_G = chi2.sf(G_square, df=v)
# H0 is accepted if X2 or G2 <= chi2_crit
