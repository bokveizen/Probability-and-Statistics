from scipy.stats import norm
import numpy as np

alpha = 0.01
# population A
n = 720
x = 168
p_A_hat = x / n
# population B
m = 760
y = 204
p_B_hat = y / m
# pooled
p_hat = (x + y) / (n + m)
diff_hat = p_A_hat - p_B_hat
z_crit = norm.isf(alpha / 2)
z_stat = diff_hat / np.sqrt(p_hat * (1 - p_hat) * (1 / n + 1 / m))
p = 2 * norm.cdf(-np.abs(z_stat))
# H0: p_A = p_B is accepted if |z_stat| <= z_crit

# interval
var_A = p_A_hat * (1 - p_A_hat) / n
var_B = p_B_hat * (1 - p_B_hat) / m
var = var_A + var_B
se = np.sqrt(var)
z_interval = (diff_hat - z_crit * se, diff_hat + z_crit * se)

