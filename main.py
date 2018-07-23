from basalt_mixing import BasaltMixing
import sample_data

ratio_ratio = BasaltMixing(step_length=.01)
ratio_ratio.ratio_ratio_mixing(
    sample_data.ratio_ratio_sample1_data, sample_data.ratio_ratio_sample2_data
)
ratio_ratio.mixer()
print(ratio_ratio.mixing_data_df)
ratio_ratio.mixer_plot()