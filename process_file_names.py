import os
from os.path import isfile, join


def process_file_names(directory):
    """
    Find all the files in a directory, assuming the format "instrument_tone_xxx"
    Don't put any other files in that dir.
    :param directory: (str) Path to a directory
    :return: (2-d array) The instrument information extracted from the given directory
    """
    file_names = [f for f in os.listdir(directory) if
                  isfile(join(directory, f)) and f[0] != "."]

    file_data = [[0] * 3 for _ in range(len(file_names))]

    for i in range(len(file_names)):
        name = file_names[i]
        exploded_name = name.split("_")
        instrument = exploded_name[0]
        tone = exploded_name[1]
        file_data[i][0] = instrument
        file_data[i][1] = tone
        file_data[i][2] = join(directory, name)

    return file_data


if __name__ == "__main__":
    process_file_names("all-samples/guitar")
