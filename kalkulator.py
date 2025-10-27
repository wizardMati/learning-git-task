import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def dodawanie(a,b):
    logging.info(f"doodawanie  {a} + {b}")
    return a + b
def odejmowanie(a,b):
    logging.info(f"odejmowanie  {a} - {b}")
    return a - b
def mnozenie(a,b):
    logging.info(f"mnozenie  {a} * {b}")
    return a * b
def dzielenie(a,b):
    logging.info(f"dzielenie  {a} / {b}")
    return a / b

print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

wybor = input("Wybor: ")

x = float(input("Podaj pierwszą litere "))
y = float(input("Podaj druga litere"))

if wybor == "1":
    wynik = dodawanie(x,y)
elif wybor == "2":
    wynik = odejmowanie(x,y)
elif wybor == "3":
    wynik = mnozenie(x,y)
elif wybor == "4":
    wynik = dzielenie(x,y)
else:
    logging.warning("wzły wybor")



logging.info(f"Wynik: {wynik}")
