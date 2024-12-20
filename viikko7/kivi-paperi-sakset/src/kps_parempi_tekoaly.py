from kps import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valisti: {tokan_siirto}")
        return tokan_siirto
