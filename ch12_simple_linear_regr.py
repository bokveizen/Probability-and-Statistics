import statsmodels.api as sm
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import t, f

alpha = 0.05
X = np.log([50, 60, 70, 80])
Y = np.log([65, 51, 40, 26])
s_X = sum(X)
s_Y = sum(Y)
s_XY = np.dot(X, Y)
s_XX = np.dot(X, X)
s_YY = np.dot(Y, Y)
assert len(X) == len(Y)
n = len(X)
SXX = s_XX - s_X ** 2 / n
SYY = s_YY - s_Y ** 2 / n
SXY = s_XY - s_X * s_Y / n
b1 = SXY / SXX
b0 = np.mean(Y) - b1 * np.mean(X)
SSE = s_YY - b0 * s_Y - b1 * s_XY
res = [Y[i] - b0 + b1 * X[i] for i in range(n)]
sigma2 = SSE / (n - 2)
sigma = np.sqrt(sigma2)

res = np.array(res)
plt.scatter(X, res / sigma)
plt.show()
fig = sm.qqplot(res, line='s')
plt.show()

# inferences
t_crit_two = t.isf(alpha / 2, df=n - 2)
t_crit_one = t.isf(alpha, df=n - 2)

# inferences on b1
hypo_b1 = 0
var_b1 = sigma2 / SXX
se_b1 = np.sqrt(var_b1)
t_stat_b1 = (b1 - hypo_b1) / se_b1
# two sided, H0: b1 = hypo_b1 is accepted if |t_stat| <= t_crit
interval_b1 = (b1 - t_crit_two * se_b1, b1 + t_crit_two * se_b1)
p_b1_two = 2 * t.sf(np.abs(t_stat_b1), df=n - 2)
# one sided, H0: b1 >= hypo_b1 is accepted if t_stat >= -t_crit
# H0: b1 <= hypo_b1 is accepted if t_stat <= t_crit
interval_upper_bd_b1 = b1 + t_crit_one * se_b1
p_b1_one_geq = t.cdf(t_stat_b1, df=n - 2)
interval_lower_bd_b1 = b1 - t_crit_one * se_b1
p_b1_one_leq = t.sf(t_stat_b1, df=n - 2)

# inferences on the regression line
x_star = 1
y_hypo = 10
y_E = b0 + b1 * x_star
var_y = sigma2 * (1 / n + np.square(x_star - np.mean(X)) / SXX)
se_y = np.sqrt(var_y)
t_stat_y = (y_E - y_hypo) / se_y
# two sided
interval_y = (y_E - t_crit_two * se_y, y_E + t_crit_two * se_y)
p_y_two = 2 * t.sf(np.abs(t_stat_y), df=n - 2)
# one sided
interval_upper_bd_y = y_E + t_crit_one * se_y
p_y_one_geq = t.cdf(t_stat_y, df=n - 2)
interval_lower_bd_y = y_E - t_crit_one * se_y
p_y_one_leq = t.sf(t_stat_y, df=n - 2)

# inferences on predictions
x_pred = 1
y_pred = b0 + b1 * x_pred
var_pred = sigma2 * (1 + 1 / n + np.square(x_pred - np.mean(X)) / SXX)
se_pred = np.sqrt(var_pred)

# the analysis of variance table, H0: beta1 = 0
y_mean = np.mean(Y)
X = np.array(X)
Y = np.array(Y)
# the total sum of squares, SST = SSR + SSE, df = n - 1
SST = np.square(Y - y_mean).sum()
# the sum of squares for regression, SSR, df = n - 2
Y_hat = b0 + b1 * X
SSR = np.square(Y_hat - y_mean).sum()
# the sum of squares for error, SSE, df = 1
SSE = np.square(Y - Y_hat).sum()
# mean squares
MSR = SSR
MSE = SSE / (n - 2)  # = sigma2
F_stat = MSR / MSE
p = f.sf(F_stat, dfn=1, dfd=n - 2)
# the coefficient of determination
R2 = SSR / SST  # = 1 / (1 + SSE / SSR)
# res = [Y[i] - b0 + b1 * X[i] for i in range(n)]

# the sample correlation coefficient, aka the Pearson product moment correlation coef.
r = SXY / np.sqrt(SXX * SYY)  # r2 = R2
# H0: rou = 0, equivalent to beta1 = 0
t_stat_r = r * np.sqrt((n - 2) / (1 - np.sqrt(r)))
