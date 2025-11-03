from faker import Faker

fake = Faker("pl_PL")


class BaseContact:
    def __init__(self, imie, nazwisko, telefon_prywatny, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon_prywatny = telefon_prywatny
        self.email = email

    def __str__(self):
        return f"{self.imie} {self.nazwisko} | tel: {self.telefon_prywatny} | email: {self.email}"

    @property
    def label_length(self):
        return len(self.imie) + len(self.nazwisko)

    def contact(self):
        print(f"Wybieram numer {self.telefon_prywatny} i dzwonię do {self.imie} {self.nazwisko}.")


class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon_prywatny, email, stanowisko, firma, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon_prywatny, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def __str__(self):
        return (f"{self.imie} {self.nazwisko} | {self.firma} ({self.stanowisko}) | "
                f"tel służbowy: {self.telefon_sluzbowy} | email: {self.email}")

    def contact(self):
        print(f"Wybieram numer służbowy {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}.")


def create_contacts(card_type, quantity):
    contacts = []
    for _ in range(quantity):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        email = fake.email()
        telefon_prywatny = fake.phone_number()

        if card_type == "base":
            contact = BaseContact(imie, nazwisko, telefon_prywatny, email)
        elif card_type == "business":
            firma = fake.company()
            stanowisko = fake.job()
            telefon_sluzbowy = fake.phone_number()
            contact = BusinessContact(imie, nazwisko, telefon_prywatny, email, stanowisko, firma, telefon_sluzbowy)
        else:
            raise ValueError("Nieznany typ wizytówki! Użyj 'base' lub 'business'.")

        contacts.append(contact)
    return contacts


if __name__ == "__main__":
    wizytowki = create_contacts("business", 3)

    for w in wizytowki:
        print(w)
        w.contact()
        print(f"Długość etykiety: {w.label_length}")
        print("-" * 50)
