from utils import *
from compressor import Compressor


class FindMusic:

    def __init__(self, comp_type):
        self._db = load_db()
        self._compressor = Compressor(comp_type)

    def find(self, sample):
        db = self.db
        freq_sample = applyGetMaxFreqs(sample)
        return min([(music, self.ncd(freq_sample, db[music]))
                    for music in db], key=lambda x: x[1])[0]

    def ncd(self, x, y):

        comp_xy = self._compressor.compress(''.join([x, y]))
        comp_x = self._compressor.compress(x)
        comp_y = self._compressor.compress(y)

        return (comp_xy - min([comp_x, comp_y])) / max([comp_x, comp_y])

    @property
    def db(self):
        return self._db


if __name__ == "__main__":
    f = FindMusic("gzip")
    f.find("../samples/test.wav")
