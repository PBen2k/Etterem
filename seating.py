import kiirasok
def leultetes(asztalok):
    kiirasok.aktualallapot(asztalok)
    x = int(input("Hányadik asztalhoz szeretne ültetni?: "))
    if asztalok[x-1].foglaltsag == "igen":
        print("\nAZ ASZTAL FOGLALT!")
    elif(asztalok[x-1].foglaltsag == "nem"): 
        asztalok[x-1].foglaltsag = "igen"
