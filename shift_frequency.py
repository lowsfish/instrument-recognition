import numpy as np


def shift_frequency(array, frequency, sampling_frequency, n_samples):
    """
    Shifts the frequency spectrum.
    :param array: (python list or numpy array) Array of the frequency spectrum
    :param frequency: (float) Number of frequencies to shift.
    :param sampling_frequency: (integer) The sampling frequency use dto record the samples with.
    :param n_samples: (integer) The number of samples in the array.
    :return: (numpy array) Normalized array.
    """
    shift_factor = n_samples / sampling_frequency
    array_size = len(array)
    frequency_shift = round(shift_factor * frequency)

    shifted_fft = np.zeros(array_size)

    for i in range(array_size - abs(frequency_shift) - 1):
        if i + frequency_shift > 0:
            shifted_fft[i + frequency_shift] = array(i)

    return shifted_fft
