
TONE_SET = ["A4", "As4", "B4", "C4", "Cs4", "D4", "Ds4", "E4", "F4", "Fs4", "G4", "Gs4"]
TONE_FREQUENCY = [440.0, 446.154, 493.883, 261.626, 277.183, 293.665, 311.127, 329.628,
                  349.228, 369.994, 391.995, 415.305]
DICT_OBJECT = dict(zip(TONE_SET, TONE_FREQUENCY))


def frequency_difference(tone):
    """
    Calculates the difference in Hz between two tones.
    :param tone: (string) The tone to calculate the difference with A4 from.
    :return: (float) The calculated difference.
    """
    return DICT_OBJECT("A4") - DICT_OBJECT(tone)
