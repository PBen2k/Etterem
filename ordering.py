import kiirasok

def rendeles(menu_tetelek, asztalok):
    kiirasok.aktualallapot(asztalok)
    print("--------------------")
    kiirasok.menukiir(menu_tetelek)
    while True:
        x = (input("\nHányadik asztalhoz lesz a rendelés?"))
        if x == "":
            break
        elif asztalok[int(x)-1].foglaltsag == "nem":
            print("\nItt nincs vendég!")
            return -1
        else:
            i = (input("\nHányadik menüelemet szereté a rendeléshez adni"))
            asztalok[int(x)-1].rendelesek.append(menu_tetelek[int(i)-1])
