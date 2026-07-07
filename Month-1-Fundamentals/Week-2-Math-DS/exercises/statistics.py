import numpy as np
from scipy import stats


'''
Dataset: [15, 22, 18, 25, 20, 17, 23, 19, 24, 21]

1. Calculate mean  -- average value
2. Calculate median -- after sorting getting middle value
3. Calculate mode -- most repeated value
4. Calculate variance -- Measures how spread out the data is.
5. Calculate standard deviation
6. Calculate range
7. Calculate IQR (Q1, Q3)
8. Identify outliers (using IQR method)
'''
data = np.array([15, 22, 18, 25, 20, 17, 23, 19, 24, 21])
print(np.mean(data))
print(np.median(data))
mode,count = stats.mode(data)
print(mode)
print(np.var(data))
print(np.std(data))
print(stats.iqr(data))

'''
1. Generate 1000 samples from normal distribution (μ=0, σ=1)
2. Generate 1000 samples from normal distribution (μ=100, σ=15)
3. Plot both distributions
4. Calculate mean and std of samples
5. Compare with theoretical values
'''
