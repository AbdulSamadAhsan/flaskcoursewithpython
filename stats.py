import statistics as s
import numpy as np
marks=[10,20,30,40,50]
mean=s.mean(marks)
median=s.median(marks)
print("Mean:",mean)
print("Median",median)
data = np.array([10, 12, 13, 14, 15, 16, 100])
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
print(iqr)
lower = q1 - 1.5 * iqr
print("lower",lower)

upper = q3 + 1.5 * iqr
print("upper",upper)
outliers = data[(data < lower) | (data > upper)]
print("Outliers:", outliers)