asztalok = []
menu_tetelek = []
class Asztal:
    def __init__(self, sorszam, meret, foglaltsag, lefoglaltsag, foglalo, idopont):
        self.sorszam = sorszam
        self.meret = meret
        self.foglaltsag = foglaltsag
        self.lefoglaltsag = lefoglaltsag
        self.foglalo = foglalo
        self.idopont = idopont
        self.rendelesek = []
    def __str__(self):
        return"{} {} {} {} {} {}".format(self.sorszam,self.meret,self.foglaltsag, self.lefoglaltsag, self.foglalo,self.idopont)

class Menuelem:
    def __init__(self, szam, elem, ar):
        self.szam = szam
        self.elem = elem
        self.ar = ar
    def __str__(self):
        return"{} {} {}".format(self.szam, self.elem,self.ar)


def asztalbetolt():
    with open ('Asztalok.txt', 'rt') as file:
        for sor in file:
            sor = sor.rstrip("\n")
            asztaldata = sor.split(" ")
            a = Asztal(0,1,2,3,4,5)
            a.sorszam = asztaldata[0]
            a.meret = asztaldata[1]
            a.foglaltsag = asztaldata[2]
            a.lefoglaltsag = asztaldata[3]
            a.foglalo = asztaldata[4]
            a.idopont = asztaldata[5]
            asztalok.append(a)
    print("\nAz asztalok adatai sikeresen be lettek töltve!\n")
    return asztalok

def menubetolt():
    with open ('Menu.txt', 'rt') as file:
        for sor in file:
            sor = sor.rstrip("\n")
            menudata = sor.split(" ")
            a = Menuelem(0,1,2)
            a.szam = menudata[0]
            a.elem = menudata[1]
            a.ar = menudata[2]
            menu_tetelek.append(a)
    print("\nA menü adatai sikeresen be lettek töltve!\n")
    return menu_tetelek
