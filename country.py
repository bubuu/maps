__author__ = 'Malgorzata Targan'

class Country:
    def __init__(self):
        self._name = None
        self._capital = None
        self._latitude = None
        self._longitude = None
        self._code = None
        self._continent = None

    def set_all(self, buffer):
        self._name = buffer[0]
        self._capital = buffer[1]
        self._latitude = float(buffer[2])
        self._longitude = float(buffer[3])
        self._code = buffer[4]
        self._continent = buffer[5]
