def total_kn(radni_sati, placa):
    print("Ukupno: ", radni_sati * placa)

radni_sati = float(input("Unesite broj radnih sati: "))
placa = float(input("Unesite iznos zarade po radnom satu: "))

print("Radni sati: ", radni_sati)
print("kn/h: ", placa)
total_kn(radni_sati, placa)
