def polindrom(slowo):
    if slowo == slowo[::-1]:
        print(f"{slowo} to polindrom")
    else:
        print(f"{slowo} to nie polindrom")



kajak = polindrom("kajak")

print(kajak)