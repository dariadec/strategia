class Wojownik:
    def __init__(self):
        self._doswiadczenie = 0
        self._zycie = 50

    def __repr__(self):
        nazwa = self.__class__.__name__
        return f'{nazwa}: hp={self.zycie}, exp={self._doswiadczenie}'

    def maszeruj(self, dystans):
        nazwa = self.__class__.__name__
        print(f'{nazwa}: Przeszedłem {dystans}m')
        self._doswiadczenie += 0.02 * dystans
