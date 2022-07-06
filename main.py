import numpy as np
import matplotlib.pyplot as plt

# dataset 1
np.random.seed(192)
x = np.random.randn(1000)

# dataset 2
np.random.seed(250)
x = np.random.normal(loc=10, scale=20, size=1000)
