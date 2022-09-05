import mentesek
asztalok = []

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

def asztalmegadas():
    while True:
        sorszam = input("sorszám: ")
        if sorszam == "":
            break

        meret = input("méret: ")

        foglaltsag = input("épp foglalt?(igen/nem): ")

        lefoglaltsag = input("van foglalás az asztalra?(igen/nem): ")
        if lefoglaltsag == "igen":
            foglalo = input("foglaló:" )
            idopont = input("időpont:" )
        else:
           lefoglaltsag == "nincs"
           foglalo = "nincs"
           idopont = "nincs"      
        asztalok.append(Asztal(sorszam, meret, foglaltsag, lefoglaltsag, foglalo, idopont))
    for x in range(0, len(asztalok)):
        mentesek.asztalok_mentes(asztalok[x])
    return asztalok
