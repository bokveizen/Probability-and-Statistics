from scipy.stats import chi2
import numpy as np

alpha = 0.05
freq_list = [66, 40, 14]
n = sum(freq_list)
p_list = [f / n for f in freq_list]
# hypo, H0: pi = pi_star, for all i in [k]
k = len(freq_list)
p_star_list = [1 / k for _ in freq_list]
assert sum(p_star_list) == 1.0
expected_freq_list = [n * p for p in p_star_list]
chi2_crit = chi2.isf(alpha, df=k - 1)
# Pearson chi-square statistic
X_square = sum(np.square(freq_list[i] - expected_freq_list[i]) / expected_freq_list[i] for i in range(k))
# likelihood ratio chi-square statistic
G_square = 2 * sum(freq_list[i] * np.log(freq_list[i] / expected_freq_list[i]) for i in range(k))
p_X = chi2.sf(X_square, df=k - 1)
p_G = chi2.sf(G_square, df=k - 1)
# H0 is accepted if X2 or G2 <= chi2_crit
