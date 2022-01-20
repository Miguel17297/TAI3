import lzma
from abc import ABC, abstractmethod
import gzip

# Todo: corrigir os compressores para retornar o numero de bits

class ICompressor(ABC):

    @abstractmethod
    def compress(self, data):
        pass


class Compressor:

    def __init__(self, comp_type):
        if comp_type == "gzip":
            self._compressor = Gzip()
        elif comp_type == "lzma":
            self._compressor = Lzma()
        else:
            raise Exception(f'Invalid format: {comp_type}')

    def compress(self, data):
        return self._compressor.compress(data.encode('utf-8'))


class Gzip(ICompressor):

    def compress(self, data):
        return len(gzip.compress(data))


class Lzma(ICompressor):
    def compress(self, data):
        return len(lzma.compress(data))
