# from __builtin__ import False


class NirspecConfig:

    def __init__(self, header):
        self.header = header

    def isTheSame(self, header):
        for kwd in ['disppos', 'echlpos', 'FILTER', 'SLITNAME']:
            if self.header[kwd] != header[kwd]:
                return False
        return True

    def toString(self):
        return 'disppos={}, echlpos={}, filter={}, slitname={}'.format(
            self.header['disppos'], self.header['echlpos'],
            self.header['FILTER'], self.header['SLITNAME'])
