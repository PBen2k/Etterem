def asztalok_mentes(egy_asztal):
    with open ('Asztalok.txt', 'a') as asztalok:
        asztalok.write("{}\n".format(egy_asztal))

def menu_mentes(egy_tetel):
    with open('Menu.txt','a') as menu:
        menu.write("{}\n".format(egy_tetel))
