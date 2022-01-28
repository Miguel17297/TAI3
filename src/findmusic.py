from compressor import Compressor
import argparse
from utils import *


# TODO: Testar o sox para windows

# Nota: o gzip pode não dar os melhores resultados por causa dos headers que adiciona
class FindMusic:

    def __init__(self, comp_type):
        self._db = load_db()
        self._compressor = Compressor(comp_type)

    def find(self, sample):
        """
        Finds the name of the music more similar to the sample.
        The more similar music is the one with smallest NCD value.
        :param sample: path to music
        :return: name of most similar music
        """

        db = self.db

        freq_sample = applyGetMaxFreqs(sample)
        return min([(music, self.ncd(freq_sample, db[music]))
                    for music in db], key=lambda x: x[1])[0]

    def ncd(self, x, y):
        """
        Computes the Normalized Compression Distance between x and y
        :param x: signature of music x
        :param y: signature of music y
        :return: music distance between 0 (similar) and 1 (dissimilar)
        """

        comp_xy = self._compressor.compress(x + y)
        comp_x = self._compressor.compress(x)
        comp_y = self._compressor.compress(y)

        return (comp_xy - min([comp_x, comp_y])) / max([comp_x, comp_y])

    @property
    def db(self):
        return self._db

    def __del__(self):
        clean()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recognize a Music",
                                     usage="python3 findmusic.py --s path_to_sample -c compressor_type")

    parser.add_argument("-s", help="Path to sample audio file to analyze", type=str, required=True)
    parser.add_argument("-c", help="Type of compressor", type=str, choices=['lzma', 'gzip', 'bzip2'], default='lzma')
    parser.add_argument("-n", help="Add noise to Sample", type=float)
    parser.add_argument("--noise-type", help="Type of noise", type=str, choices=['whitenoise', 'brownnoise'])
    args = parser.parse_args()

    sample = args.s
    n = args.n
    noise_type = args.noise_type

    if args.noise_type and not args.n:  # to select noise type is necessary to select noise value first
        parser.error('--noise_type requires -n')

    elif args.n and not args.noise_type:
        noise_type = 'whitenoise'

    _, extension = os.path.splitext(sample)

    assert extension == ".wav", f'Invalid format: {extension}'  # sample must be in .wav format

    if args.n:
        sample = add_noise(sample, args.n, args.noise_type)  # add noise to sample

    assert os.path.exists(sample), f'Invalid file: {sample}'

    f = FindMusic(args.c)

    print(f"For target sample:{sample} we got {f.find(sample)}")
