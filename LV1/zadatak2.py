ocjena = 1.1
while ocjena < 0 or ocjena > 1:
    ocjena = float(input("Unesite ocjenu u intervalu od 0.0 do 1.0: "))

if ocjena >= 0.9:
    print("A")
elif ocjena >= 0.8:
    print("B")
elif ocjena >= 0.7:
    print("C")
elif ocjena >= 0.6:
    print("D")
else:
    print("F")






