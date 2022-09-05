def szamlazas(menu_tetelek, asztalok):
    x = int(input("\nHányadik asztalhoz szeretne számlát nyomtatni? "))
    print("--------------------SZÁMLA--------------------")
    print("\nA {}. asztal rendelései:\n".format(asztalok[x-1].sorszam))
    for i in range(0, len(asztalok[x-1].rendelesek)):
        print(asztalok[x-1].rendelesek[i])

    osszeg = 0
    print("A {}. számú asztal számlájának végösszege:\n".format(asztalok[x-1].sorszam))
    for i in range(0, len(asztalok[x-1].rendelesek)):
        osszeg += int(asztalok[x-1].rendelesek[i].ar)
    print(osszeg, "Forint")
    asztalok[x-1].rendelesek = []
    asztalok[x-1].foglaltsag = "nem"
    print("--------------------SZÁMLA--------------------")
    print("\nA {}. számú asztal számlája rendezve lett, rendelések törölve, a vendég távozott!".format(asztalok[x-1].sorszam))
