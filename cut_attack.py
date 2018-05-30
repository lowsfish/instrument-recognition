import soundfile as sf
import sys
import numpy as np
import math


def db2mag(db):
    return np.power(10, db / 20)


def cut_attack(audio_file, attack_length_ms):
    """
    Seperates the signal into one with only attack and one without
    :param audio_file: The path to the file.
    :param attack_length_ms: The attack length in milliseconds
    :return only_attack: (a numpy 1-d array) The signal with the attack separated
    :return without_attack: (a numpy 1-d array) The signal without the attack
    """
    try:
        data, sample_rate = sf.read(audio_file)
    except RuntimeError:
        print("Cannot open file!")
        sys.exit()

    frame_ms = 10
    frame_width = sample_rate / 1000 * frame_ms
    num_samples = len(data)
    num_frames = int(math.floor(num_samples / frame_width))
    energy = np.zeros(num_frames)
    start_sample = np.zeros(num_frames, dtype=int)
    end_sample = np.zeros(num_frames, dtype=int)

    for frame in range(num_frames):
        start_sample[frame] = int(frame * frame_width + 1)
        end_sample[frame] = int((frame + 1) * frame_width)
        frame_index = range(start_sample[frame], end_sample[frame] + 1)
        energy[frame] = sum(np.square(data[frame_index]))

    signal_energy = np.sqrt(np.mean(data ** 2))

    onset_db_threshold = 10
    onset_start_index = np.where(energy > signal_energy *
                                          db2mag(onset_db_threshold))[0][0]
    onset_start_seconds = onset_start_index * (frame_ms / 1000)

    t = np.linspace(0, len(data) / sample_rate, len(data))
    only_attack = data[(t > onset_start_seconds) & (t < onset_start_seconds +
                                                    attack_length_ms / 1000)]

    without_onset_shift_s = 0.2
    without_attack = data[(t > onset_start_seconds + attack_length_ms / 1000 + without_onset_shift_s)
                          & (t < len(data) / sample_rate)]
    return only_attack, without_attack


if __name__ == "__main__":
    cut_attack("all-samples/guitar/guitar_A2_very-long_forte_normal.wav", 100)
