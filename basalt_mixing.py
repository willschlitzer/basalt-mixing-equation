import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sample_data import ratio_ratio_sample1_data, ratio_ratio_sample2_data


def ratio_ratio_mixing(sample1_data, sample2_data):
    """Creates the variables for 2 element or isotope ratios"""
    x1 = sample1_data[0] / sample1_data[1]
    y1 = sample1_data[2] / sample1_data[3]
    x2 = sample2_data[0] / sample2_data[1]
    y2 = sample2_data[2] / sample2_data[3]
    # a1 and a2 are the denominators for the y-axis ratios
    # b1 and b2 are the denominators for the x-axis ratios
    a1 = sample1_data[3]
    b1 = sample1_data[1]
    a2 = sample2_data[3]
    b2 = sample2_data[1]
    # A, B, C, D are coefficients for the mixing equation
    A = a2 * b1 * y2 - a1 * b2 * y1
    B = a1 * b2 - a2 * b1
    C = a2 * b1 * x1 - a1 * b2 * x2
    D = a1 * b2 * x2 * y1 - a2 * b1 * x1 * y2
    return x1, y1, x2, y2, A, B, C, D


def ratio_element_mixing(sample1_data, sample2_data):
    """Creates the variables for a ratio/ratio and element"""
    x1 = sample1_data[0]
    y1 = sample1_data[1] / sample2_data[2]
    x2 = sample2_data[0]
    y2 = sample2_data[1] / sample3_data[2]
    # b=1 since the denominators for the x-axis are 1
    # a1 and a2 are the denominators for the y-axis ratios
    a1 = sample1_data[2]
    a2 = sample2_data[2]
    # A, B, C, D are coefficients for the mixing equation
    A = a2 * y2 - a1 * y1
    B = a1 - a2
    C = a2 * x1 - a1 * x2
    D = a1 * x2 * y1 - a2 * x1 * y2
    return x1, y1, x2, y2, A, B, C, D


def element_element_mixing(sample1_data, sample2_data):
    """Create the variables for an element-element mixing"""
    x1 = sample1_data[0]
    y1 = sample1_data[1]
    x2 = sample2_data[0]
    y2 = sample2_data[1]
    # a=1. b=1 since the denominators for the x-axis, y-axis are 1
    # A, B, C, D are coefficients for the mixing equation
    A = y2 - y1
    B = 0
    C = x1 - x2
    D = x2 * y1 - x1 * y2
    return x1, y1, x2, y2, A, B, C, D


def mixer(sample1_data, sample2_data):
    """Generates the mixing data based upon the sample"""
    # The mixing percentage elapsed between calculations
    step_length = .1
    x1, y1, x2, y2, A, B, C, D = ratio_ratio_mixing(sample1_data, sample2_data)
    # Creates the current percentage elapsed variable
    current_step = 0  # 0% mixed at the beginning
    # Creates an empty list that will hold the data
    mixing_data = []
    while current_step <= 1:
        # Creates the current x-value based upon mixing percentage
        x = x1 * current_step + x2 * (1 - current_step)
        # Determines the y-value based upon x-value
        y = (-(A * x) - D) / (B * x + C)
        # Appends current percentage to list
        mixing_data.append([current_step, x, y])
        # Advances to next mixing percentage
        current_step += step_length
    mixing_data_array = np.array(mixing_data)
    mixing_data_df = pd.DataFrame(mixing_data_array, columns=["current_step", "x", "y"])
    return mixing_data_df


# A demonstration of test data
df = mixer(ratio_ratio_sample1_data, ratio_ratio_sample2_data)
df.plot("x", "y")
print(df)
plt.show()
