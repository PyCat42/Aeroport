import re

datoteka_a = "C:/Users/HP/PycharmProjects/Stvar1/avioni.txt"
with open(datoteka_a, "r", encoding="UTF-8") as avioni:
    recnik_avioni = {}
    sablon_avioni = re.compile(r"\s*[:]\s*")
    for linija_a in avioni:
        linija_bez_razmaka = linija_a.strip()
        tip, sedista = sablon_avioni.split(linija_bez_razmaka)
        recnik_avioni[tip] = int(sedista)

datoteka_l = "C:/Users/HP/PycharmProjects/Stvar1/letovi1.txt"
with open(datoteka_l, "r", encoding="UTF-8") as letovi:
    recnik_letovi = {}
    sablon1 = re.compile(r"\s*[:,]\s*")
    for linija_l in letovi:
        linija_bez_razmaka = linija_l.strip()
        grad, let, avion = sablon1.split(linija_bez_razmaka)
        if not grad in recnik_letovi.keys():
            recnik_letovi[grad] = [[avion], [let]]
        else:
            recnik_letovi[grad][0] += ", " + avion
            recnik_letovi[grad][1] += ", " + let

while True:
    try:
        zeljeni_grad = input("Unesite zeljeni grad: ")
        if not zeljeni_grad: break
        ukupno = 0
        avioni = recnik_letovi[zeljeni_grad][0]
        for i in avioni:
            ukupno += recnik_avioni[i]
        print(ukupno)
    except KeyError:
        print("Nema letova za dati grad!")

