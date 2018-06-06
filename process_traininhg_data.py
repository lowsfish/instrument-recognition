import soundfile as sf
import numpy as np

from cut_attack import cut_attack
from process_file_names import process_file_names
from frequency_difference import frequency_difference
from shift_frequency import shift_frequency
from create_feature_vector import create_feature_vector
from normalize_data import normalize_data


def process_training_data(directory, n_chunks, cut_attack_conf):
    file_data = process_file_names(directory)
    training_data = [[0] * 2 for _ in range(len(file_data))]
    onset_length_ms = 100

    for i in range(len(file_data)):
        print("{:d} of {:d}", i, len(file_data))
        filename = file_data[i][2]

        try:
            data, sample_rate = sf.read(filename)
        except RuntimeError:
            print("Cannot open file {}".format(filename))
            exit()

        if not cut_attack_conf:
            only_attack, without_attack = cut_attack(filename, onset_length_ms)

            if cut_attack_conf is "only_attack":
                data = only_attack
            elif cut_attack_conf is "without_attack":
                data = without_attack
            else:
                print("cut_attack_conf Error! Must be \"only_attack\" or \"without_attack\"")
                exit()

        n_samples = len(data)

        # do Fourier Transform
        y_fft = abs(np.fft.fft(data))
        y_fft = y_fft[:n_samples // 2]
        f = sample_rate * np.array(range(n_samples)) / n_samples
        f = f[1:round(1000 * n_samples / sample_rate)]

        tone = file_data[i][1]
        frequency_diff = frequency_difference(tone)
        shifted_fft = shift_frequency(y_fft, frequency_diff, sample_rate, n_samples)

        shifted_fft = shifted_fft[:round(1000 * n_samples / sample_rate)]

        feature_vector = create_feature_vector(shifted_fft, n_chunks)
        feature_vector = normalize_data(feature_vector)

        training_data[i][0] = file_data[i][0]
        training_data[i][1] = feature_vector

    input_data = [row[1] for row in training_data]
    input_data = list(map(list, zip(*input_data)))  # transpose
    label_data = [row[0] for row in training_data]

    instrument_set = set(label_data)
    instrument_value = list(range(len(instrument_set)))
    instruction_label_map = dict(zip(instrument_set, instrument_value))

    mapped_label_data = np.zeros((len(instrument_set), len(label_data)))

    for i in range(len(label_data)):
        instrument = label_data[i]
        mapped_label_data[instruction_label_map[instrument]][i] = 1

    return input_data, mapped_label_data.tolist()
