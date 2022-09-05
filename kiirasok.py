def aktualallapot(asztalok):
    print()
    for x in range (0,len(asztalok)):
        if(asztalok[x].foglaltsag == "igen" and asztalok[x].lefoglaltsag == "nem"):
            print("A {}. asztal foglalt, {} férőhelyes, és nincs rá lefoglalás.\n".format(asztalok[x].sorszam, asztalok[x].meret))

        elif(asztalok[x].foglaltsag == "nem" and asztalok[x].lefoglaltsag == "igen"):
            print("A {}. asztal nem foglalt, {} férőhelyes, de {}-re le van foglalva {} által.\n".format(asztalok[x].sorszam, asztalok[x].meret, asztalok[x].idopont, asztalok[x].foglalo))

        elif(asztalok[x].foglaltsag == "igen" and asztalok[x].lefoglaltsag == "igen"):
            print("A {}. asztal foglalt, {} férőhelyes, és {}-tól van lefoglalva {} által.\n".format(asztalok[x].sorszam, asztalok[x].meret, asztalok[x].idopont, asztalok[x].foglalo))

        else:
            print("A {}. asztal nem foglalt, {} férőhelyes, és nincs lefoglalva.\n".format(asztalok[x].sorszam, asztalok[x].meret))


def menukiir(menu_tetelek):
    print()
    for x in range (0,len(menu_tetelek)):
        print("{}. {} {} HUF".format(menu_tetelek[x].szam, menu_tetelek[x].elem, menu_tetelek[x].ar))
