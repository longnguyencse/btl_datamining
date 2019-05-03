import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A = np.array([[1, 2], [3, 4]])
print(A)
print("Done")

peoples_df = pd.read_csv('../data/result.csv')
peoples_df.head(5)
print(peoples_df.head(5))