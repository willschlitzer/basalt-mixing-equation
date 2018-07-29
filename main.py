from basalt_mixing import BasaltMixing
from sample_data import *

ratio_ratio = BasaltMixing(
    step_length=.01,
    sample1_data=string_ratio_ratio_sample1_data,
    x_label=ratio_ratio_x_label,
    sample2_data=ratio_ratio_sample2_data,
    y_label=ratio_ratio_y_label,
)

ratio_ratio.mixer()
print(ratio_ratio.mixing_data_df)
ratio_ratio.mixer_plot()
