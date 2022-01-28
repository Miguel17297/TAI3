import os

from src.comp_type import CompType
from src.findmusic import FindMusic

import matplotlib.pyplot as plt

SAMPLES_PATH = ''


def read_samples(filepath):
    return [os.path.join(filepath, filename) for filename in os.listdir(filepath)]


def get_accuracy(f, samples):
    acc = 0
    for sample in samples:
        actual_song = sample[15:-13]
        song_found = f.find(sample)
        print(f'Compare "{actual_song}" to "{song_found}"')
        if actual_song in song_found:
            acc += 1
    return acc / len(samples)


def stats_compressors(samples_10):
    compressor_acc = []
    compressors = ['gzip', 'lzma']
    for compressor in compressors:
        f = FindMusic(compressor)
        acc = get_accuracy(f, samples_10)
        print(f'Acc for samples_10 and GZIP {acc}')
        compressor_acc.append(acc * 100)
    # print(f"For target sample:{sample} we got {f.find(sample)}")

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(compressors, compressor_acc, color='maroon',
            width=0.4)

    plt.xlabel("Compressor")
    plt.ylabel("Accuracy(%)")
    plt.title("Accuracy by type of Compressor")
    plt.show()


def stats_sample_size(samples_10, samples_20, samples_30,compressor):
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


def main():
    samples = read_samples('..\samples_raw')
    samples_10 = [sample for sample in samples if '10' in sample[-6:]]
    samples_20 = [sample for sample in samples if '20' in sample[-6:]]
    samples_30 = [sample for sample in samples if '30' in sample[-6:]]

    stats_compressors(samples_20)
    stats_sample_size(samples_10, samples_20, samples_30, 'lzma')
    stats_sample_size(samples_10, samples_20, samples_30, 'gzip')




if __name__ == '__main__':
    main()
