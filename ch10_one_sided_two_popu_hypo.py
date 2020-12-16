from scipy.stats import norm
import numpy as np

alpha = 0.05
H0_type = 0
# population A
n = 400
x = 29
p_A_hat = x / n
# population B
m = 320
y = 14
p_B_hat = y / m
# pooled
p_hat = (x + y) / (n + m)
diff_hat = p_A_hat - p_B_hat
z_crit = norm.isf(alpha)
z_stat = diff_hat / np.sqrt(p_hat * (1 - p_hat) * (1 / n + 1 / m))

if H0_type:  # H0: p_A >= p_B
    p = norm.cdf(z_stat)
    # H0 is accepted if z_stat >= -z_crit
else:  # H0: p_A <= p_B
    p = 1 - norm.cdf(z_stat)
    # H0 is accepted if z_stat <= z_crit

# interval
var_A = p_A_hat * (1 - p_A_hat) / n
var_B = p_B_hat * (1 - p_B_hat) / m
var = var_A + var_B
se = np.sqrt(var)
z_interval_upper_bd = diff_hat + z_crit * se
z_interval_lower_bd = diff_hat - z_crit * se
