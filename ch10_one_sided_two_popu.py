from scipy.stats import norm
import numpy as np

alpha = 0.05
# population A
n = 33
x = 19
p_A_hat = x / n
# population B
m = 30
y = 15
p_B_hat = y / m
# hypo
p_A = 0.5
p_B = 0.5

diff_hat = p_A_hat - p_B_hat
diff = p_A - p_B
var_A = p_A_hat * (1 - p_A_hat) / n
var_B = p_B_hat * (1 - p_B_hat) / m
var = var_A + var_B

se = np.sqrt(var)
z_crit = norm.isf(alpha)
z_interval_upper_bd = diff_hat + z_crit * se
z_interval_lower_bd = diff_hat - z_crit * se

z_stat = (diff_hat - diff) / np.sqrt(var)
# H0: p_A = p_B, pooled estimate
p_hat = (x + y) / (n + m)
z_stat_pooled = diff_hat / np.sqrt(p_hat * (1 - p_hat) * (1 / n + 1 / m))
