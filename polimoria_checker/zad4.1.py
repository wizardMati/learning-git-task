def polindrom(slowo):
    if slowo == slowo[::-1]:
        print(f"{slowo} to polindrom")
    else:
        print(f"{slowo} to nie polindrom")



woda = polindrom("woda")
print(woda)

kajak = polindrom("kajak")

print(kajak)