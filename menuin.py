import mentesek
menu_tetelek =[]

class Menuelem:
    def __init__(self, szam, elem, ar):
        self.szam = szam
        self.elem = elem
        self.ar = ar
    def __str__(self):
        return"{} {} {}".format(self.szam, self.elem,self.ar)

def menumegadas():
    while True:
        szam = input("szám: ")
        if szam == "":
            break
        elem = input("étel/ital: ")
        ar = input("ár: ")
        menu_tetelek.append(Menuelem(szam, elem, ar))
    for x in range(0, len(menu_tetelek)):
        mentesek.menu_mentes(menu_tetelek[x])
    return menu_tetelek
