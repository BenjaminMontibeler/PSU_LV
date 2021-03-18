ocjena = 1.1
while ocjena < 0 or ocjena > 1:
    try:
        ocjena = float(input("Unesite ocjenu u intervalu od 0.0 do 1.0: "))
        if ocjena > 1.0:
            print("Izvan intervala!")
        elif ocjena >= 0.9:
            print("A")
        elif ocjena >= 0.8:
            print("B")
        elif ocjena >= 0.7:
            print("C")
        elif ocjena >= 0.6:
            print("D")
        elif ocjena >=0:
            print("F")
        else:
            print("Izvan intervala!")
    except ValueError:
        print("Ocjena mora biti broj!")






