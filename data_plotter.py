import basalt_mixing
import matplotlib.pyplot as plt

from sample_data import ratio_ratio_sample1_data, ratio_ratio_sample2_data

# A demonstration of test data
df = basalt_mixing.mixer(ratio_ratio_sample1_data, ratio_ratio_sample2_data)
df.plot("x", "y")
print(df)
plt.show()