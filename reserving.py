import kiirasok
import mentesek
def foglalas(asztalok):
    kiirasok.aktualallapot(asztalok)
    x = int (input("\nHányadik asztalhoz szeretne foglalást rögzíteni?: "))
    asztalok[x-1].lefoglaltsag = "igen"
    asztalok[x-1].foglalo = input("Foglaló neve: ")
    asztalok[x-1].idopont = input("Időpont:" )
    for i in range(0, len(asztalok)):
        mentesek.asztalok_mentes(asztalok[i]) 
