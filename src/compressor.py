from abc import ABC, abstractmethod
import lzma
import gzip
import bz2

# Todo: corrigir os compressores para retornar o numero de bits

class ICompressor(ABC):

    @abstractmethod
    def compress(self, data):
        """
        Computes the number of bytes to compress the data

        :param data: object to be compressed
        :return: number of bytes to compress the data
        """
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
        return self._compressor.compress(data)


class Gzip(ICompressor):
    """
     GZip Compressor
    """

    def compress(self, data):
        return len(gzip.compress(data))


class Lzma(ICompressor):
    """
    Lzma Compressor
    """
    def compress(self, data):
        return len(lzma.compress(data))

class Bzip2(ICompressor):
    """
    Bzip2 Compressor
    """
    def compress(self, data):
        return len(bz2.compress(data))
