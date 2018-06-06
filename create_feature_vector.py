import numpy as np


def create_feature_vector(frequency_array, n_chunks):
    """
    Creates a feature vector from an array with given amount of elements.
    :param frequency_array: (python list or numpy array) The array of
                            frequencies from the frequency spectrum
    :param n_chunks: (integer) The number of chunks/elements to take the
                    average over and construct the feature vector with
    :return: (numpy array) The feature vector.
    """
    feature_vector = np.zeros(n_chunks)
    chunk_size = floor(len(frequency_array) / n_chunks)

    for i in range(n_chunks):
        chunk = frequency_array[1 + i * chunk_size:(n + 1) * chunk_size]
        chunk_average = np.mean(chunk)
        feature_vector[i] = chunk_average

    return feature_vector
