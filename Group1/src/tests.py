import os

import numpy as np

from src.comp_type import CompType

from src.findmusic import FindMusic
import matplotlib.pyplot as plt

from src.utils import add_noise

SAMPLES_PATH = ''


def read_samples(filepath):
    return [os.path.join(filepath, filename) for filename in os.listdir(filepath)]


def get_accuracy(f, samples, noise=None, noise_type=None):
    acc = 0
    for sample in samples:
        actual_song = sample[15:-13]
        if noise is not None:
            sample = add_noise(sample, noise, noise_type)
        song_found = f.find(sample)
        if actual_song in song_found:
            acc += 1
    return acc / len(samples)


def stats_compressors(samples_10):
    compressor_acc = []
    compressors = ['gzip', 'lzma', 'bzip2']
    for compressor in compressors:
        f = FindMusic(compressor)
        acc = get_accuracy(f, samples_10)
        compressor_acc.append(acc * 100)

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(compressors, compressor_acc, color='maroon',
            width=0.4)

    plt.xlabel("Compressor")
    plt.ylabel("Accuracy(%)")
    plt.title("Accuracy by type of Compressor")
    plt.show()


def stats_sample_size(samples_10, samples_20, samples_30, compressor):
    samples_acc = []
    for samples in [samples_10, samples_20, samples_30]:
        f = FindMusic(compressor)
        acc = get_accuracy(f, samples)
        samples_acc.append(acc * 100)

    plt.plot([10, 20, 30], samples_acc)
    plt.xlabel("Sample Size(s)")
    plt.ylabel("Accuracy(%)")
    plt.title(f"Accuracy by Sample Size (for {compressor.upper()} Compressor)")
    plt.show()


def stats_noise(samples_20, compressor, noise_type):
    samples_acc = []

    for noise in [-0.4, -0.3, -0.2, -0.1, -0.05, 0, 0.05, 0.1, 0.2, 0.3, 0.4]:
        f = FindMusic(compressor)
        acc = get_accuracy(f, samples_20, noise, noise_type)
        samples_acc.append(acc * 100)

    plt.plot([-0.4, -0.3, -0.2, -0.1, -0.05, 0, 0.05, 0.1, 0.2, 0.3, 0.4], samples_acc)
    plt.xlabel("Noise Level")
    plt.ylabel("Accuracy(%)")
    plt.title(f"Accuracy by Noise Level for {compressor.upper()} Compressor (using {noise_type[0].upper() + noise_type[1:]})")
    plt.show()


def main():
    samples = read_samples('..\samples_raw')
    samples_10 = [sample for sample in samples if '10' in sample[-6:]]
    samples_20 = [sample for sample in samples if '20' in sample[-6:]]
    samples_30 = [sample for sample in samples if '30' in sample[-6:]]

    stats_compressors(samples_20)
    stats_sample_size(samples_10, samples_20, samples_30, 'lzma')
    stats_sample_size(samples_10, samples_20, samples_30, 'gzip')
    stats_sample_size(samples_10, samples_20, samples_30, 'bzip2')
    stats_noise(samples_30, 'bzip2', 'whitenoise')
    stats_noise(samples_30, 'bzip2', 'brownnoise')



if __name__ == '__main__':
    main()
