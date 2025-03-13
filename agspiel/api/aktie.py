#  Copyright (c) 2021 | KingKevin23 (@kingkevin023)

class Aktie:
    def __init__(self, wkn: int, stueckzahl: int):
        self.wkn: int = wkn
        self.stueckzahl: int = stueckzahl

    def to_dict(self) -> dict:
        """
        Returns a dict of all properties to dump self as json
        """
        return {
            prop: getattr(self, prop)
            for prop in dir(self)
            if isinstance(getattr(type(self), prop, None), property)
        }

    @property
    def wkn(self) -> int:
        return self._wkn

    @wkn.setter
    def wkn(self, value: int):
        self._wkn = value

    @property
    def stueckzahl(self) -> int:
        return self._stueckzahl

    @stueckzahl.setter
    def stueckzahl(self, value: int):
        self._stueckzahl = value


class Aktionaer(Aktie):
    def __init__(self, wkn: int, stueckzahl: int):
        super().__init__(wkn, stueckzahl)