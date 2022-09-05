import asztalin
import menuin
import seating
import ordering
import billing
import kiirasok
import reserving
import betoltesek
def main():
    while True:
        print("-------------------------",
                "0: Asztalok megadása",
                "1: Menü megadása",
                "2: Vendég leültetése",
                "3: Rendelés felvétele",
                "4: Számlázás",
                "5: Aktuális állapot",
                "6: Menü kiírása",
                "7: Foglalás rögzítése",
                "8: Asztalok betöltése fájlból",
                "9: Menü betöltése fájlból",
                "10:kilépés",
                sep="\n")

        try:
            x = int(input("kívánt menüpont: "))
            if x ==10:
                break
            elif x == 0:
                asztalok = asztalin.asztalmegadas()
            elif x == 1:
                menu_tetelek = menuin.menumegadas()
            elif x == 2:
                seating.leultetes(asztalok)
            elif x == 3:
                ordering.rendeles(menu_tetelek, asztalok)
            elif x == 4:
                billing.szamlazas(menu_tetelek, asztalok)
            elif x == 5:
                kiirasok.aktualallapot(asztalok)
            elif x == 6:
                kiirasok.menukiir(menu_tetelek)
            elif x == 7:
                reserving.foglalas(asztalok)
            elif x == 8:
                asztalok = betoltesek.asztalbetolt()
            elif x == 9:
                menu_tetelek = betoltesek.menubetolt()
        except:
            ValueError
            print("\n----------VALAMI HIBA TÖRTÉNT, PRÓBÁLJA ÚJRA!----------\n")
            
main()
