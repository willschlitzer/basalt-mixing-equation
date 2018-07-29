import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


class BasaltMixing:
    def __init__(
        self, step_length, sample1_data, x_label, sample2_data, y_label
    ):
        self.step_length = step_length
        if not os.path.isdir("data/"):
            os.mkdir("data")
        self.sample1_data = sample1_data
        self.x_label = x_label
        self.sample2_data = sample2_data
        self.y_label = y_label
        self.data_validity_test()

    def data_validity_test(self):
        """Determines if sample data only contains integers or floats, and is the correct length"""
        for item in self.sample1_data + self.sample2_data:
            assert type(item) == float or type(item) == int
        self.length1 = len(self.sample1_data)
        self.length2 = len(self.sample2_data)
        if (self.length1 == self.length2) and (
            (self.length1 == 4) or (self.length1 == 3) or (self.length1 == 2)
        ):
            self.mixing_model_selector()

    def mixing_model_selector(self):
        "Runs the correct mixing model based upon the length of the data"
        if self.length1 == 4:
            self.ratio_ratio_mixing()
        elif self.length1 == 3:
            self.ratio_elelement_mixing()
        else:
            self.element_element_mixing()

    def ratio_ratio_mixing(self):
        """Creates the variables for 2 element or isotope ratios"""
        self.x1 = self.sample1_data[0] / self.sample1_data[1]
        self.y1 = self.sample1_data[2] / self.sample1_data[3]
        self.x2 = self.sample2_data[0] / self.sample2_data[1]
        self.y2 = self.sample2_data[2] / self.sample2_data[3]
        # a1 and a2 are the denominators for the y-axis ratios
        # b1 and b2 are the denominators for the x-axis ratios
        a1 = self.sample1_data[3]
        b1 = self.sample1_data[1]
        a2 = self.sample2_data[3]
        b2 = self.sample2_data[1]
        # A, B, C, D are coefficients for the mixing equation
        self.A = a2 * b1 * self.y2 - a1 * b2 * self.y1
        self.B = a1 * b2 - a2 * b1
        self.C = a2 * b1 * self.x1 - a1 * b2 * self.x2
        self.D = a1 * b2 * self.x2 * self.y1 - a2 * b1 * self.x1 * self.y2

    def ratio_element_mixing(self):
        """Creates the variables for a ratio/ratio and element"""
        self.x1 = self.sample1_data[0]
        self.y1 = self.sample1_data[1] / self.sample1_data[2]
        self.x2 = self.sample2_data[0]
        self.y2 = self.sample2_data[1] / self.sample2_data[2]
        # b=1 since the denominators for the x-axis are 1
        # a1 and a2 are the denominators for the y-axis ratios
        a1 = self.sample1_data[2]
        a2 = self.sample2_data[2]
        # A, B, C, D are coefficients for the mixing equation
        self.A = a2 * self.y2 - a1 * self.y1
        self.B = a1 - a2
        self.C = a2 * self.x1 - a1 * self.x2
        self.D = a1 * self.x2 * self.y1 - a2 * self.x1 * self.y2

    def element_element_mixing(self):
        """Create the variables for an element-element mixing"""
        self.x1 = self.sample1_data[0]
        self.y1 = self.sample1_data[1]
        self.x2 = self.sample2_data[0]
        self.y2 = self.sample2_data[1]
        # a=1. b=1 since the denominators for the x-axis, y-axis are 1
        # A, B, C, D are coefficients for the mixing equation
        self.A = self.y2 - self.y1
        self.B = 0
        self.C = self.x1 - self.x2
        self.D = self.x2 * self.y1 - self.x1 * self.y2

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
