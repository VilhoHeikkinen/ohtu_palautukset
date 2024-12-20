from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peli(peli):
    if peli == "PVP":
        return KPSPelaajaVsPelaaja()
    elif peli == "tekoaly":
        return KPSTekoaly()
    elif peli == "ptekoaly":
        return KPSParempiTekoaly()