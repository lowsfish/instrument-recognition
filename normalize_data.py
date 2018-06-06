import numpy as np


def normalize_data(input_data):
    """
    Normalizes the input using feature scaling.
    :param input_data: (numpy array or python list) The array to perform
                        normalizing on.
    :return: (numpy array) Normalized array.
    """
    max_v = max(input_data)
    min_v = min(input_data)
    normalized_data = np.zeros(len(input_data))

    for i in range(len(input_data)):
        normalized_data[i] = (input_data[i] - min_v) / (max_v - min_v)

    return normalized_data
