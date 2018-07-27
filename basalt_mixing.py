import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


class BasaltMixing:
    def __init__(self, step_length):
        self.step_length = step_length
        if not os.path.isdir("data/"):
            os.mkdir("data")

    def ratio_ratio_mixing(self, sample1_data, sample2_data):
        """Creates the variables for 2 element or isotope ratios"""
        assert len(sample1_data) == 4 and len(sample2_data) == 4
        self.x1 = sample1_data[0] / sample1_data[1]
        self.y1 = sample1_data[2] / sample1_data[3]
        self.x2 = sample2_data[0] / sample2_data[1]
        self.y2 = sample2_data[2] / sample2_data[3]
        # a1 and a2 are the denominators for the y-axis ratios
        # b1 and b2 are the denominators for the x-axis ratios
        a1 = sample1_data[3]
        b1 = sample1_data[1]
        a2 = sample2_data[3]
        b2 = sample2_data[1]
        # A, B, C, D are coefficients for the mixing equation
        self.A = a2 * b1 * self.y2 - a1 * b2 * self.y1
        self.B = a1 * b2 - a2 * b1
        self.C = a2 * b1 * self.x1 - a1 * b2 * self.x2
        self.D = a1 * b2 * self.x2 * self.y1 - a2 * b1 * self.x1 * self.y2

    def ratio_element_mixing(self, sample1_data, sample2_data):
        """Creates the variables for a ratio/ratio and element"""
        assert len(sample1_data) == 3 and len(sample2_data) == 3
        self.x1 = sample1_data[0]
        self.y1 = sample1_data[1] / sample2_data[2]
        self.x2 = sample2_data[0]
        self.y2 = sample2_data[1] / sample3_data[2]
        # b=1 since the denominators for the x-axis are 1
        # a1 and a2 are the denominators for the y-axis ratios
        a1 = sample1_data[2]
        a2 = sample2_data[2]
        # A, B, C, D are coefficients for the mixing equation
        self.A = a2 * y2 - a1 * y1
        self.B = a1 - a2
        self.C = a2 * x1 - a1 * x2
        self.D = a1 * x2 * y1 - a2 * x1 * y2

    def element_element_mixing(self, sample1_data, sample2_data):
        """Create the variables for an element-element mixing"""
        assert len(sample1_data) == 2 and len(sample2_data) == 2
        self.x1 = sample1_data[0]
        self.y1 = sample1_data[1]
        self.x2 = sample2_data[0]
        self.y2 = sample2_data[1]
        # a=1. b=1 since the denominators for the x-axis, y-axis are 1
        # A, B, C, D are coefficients for the mixing equation
        self.A = y2 - y1
        self.B = 0
        self.C = x1 - x2
        self.D = x2 * y1 - x1 * y2

    def mixer(self):
        """Generates the mixing data based upon the sample"""
        # Creates the current percentage elapsed variable
        current_step = 0  # 0% mixed at the beginning
        # Creates an empty list that will hold the data
        self.mixing_data = []
        while current_step < 1.00001:
            # Creates the current x-value based upon mixing percentage
            x = self.x1 * current_step + self.x2 * (1 - current_step)
            # Determines the y-value based upon x-value
            y = (-(self.A * x) - self.D) / (self.B * x + self.C)
            # Appends current percentage to list
            percent_mixed = current_step * 100
            self.mixing_data.append([percent_mixed, x, y])
            # Advances to next mixing percentage
            current_step += self.step_length
        self.mixing_data_array = np.array(self.mixing_data)
        self.mixing_data_df = pd.DataFrame(
            self.mixing_data_array, columns=["percent_mixed", "x", "y"]
        )
        self.mixing_data_df.to_csv("data/run_data.csv")

    def mixer_plot(self):
        self.mixing_data_df.plot("x", "y")
        plt.savefig("data/run_chart.png")
