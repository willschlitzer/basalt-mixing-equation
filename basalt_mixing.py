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
