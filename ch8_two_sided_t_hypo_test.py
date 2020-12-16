from scipy.stats import t
import numpy as np

# H_0: \mu = \mu_0 versus H_A: \mu \neq \mu_0
mu0 = 58
alpha = 0.05
mean = 60  # x bar
s = 22  # sample std
n = 121.0  # sample size

df = n - 1
# \mu \in x bar \pm t_{\alpha/2, n-1} s / \sqrt{n}
t_stat = np.sqrt(n) * (mean - mu0) / s
p = 2 * t.sf(np.abs(t_stat), df=df)
