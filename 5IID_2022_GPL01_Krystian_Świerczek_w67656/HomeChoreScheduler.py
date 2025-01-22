from collections import deque

class Zadania: # Klasa do tworzenia obiektu zadań z nazwą zadania i czasem jego trwania
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class Rodzina: # Klasa z funkcjami do tworzenia obiektu członka rodziny z danymi i rzeczy związanych z zadaniami i preferencjami
    def __init__(self, name, availability, preferences=None):
        self.name = name
        self.availability = availability
        self.preferences = preferences if preferences else []
        self.assigned_chores = []

    def assign_chore(self, chore):
        self.assigned_chores.append(chore)
        self.availability -= chore.duration

    def prefers(self, chore):
        return chore.name in self.preferences

    def __str__(self):
        assigned = "\n  ".join([f"{chore.name} ({chore.duration}h)" for chore in self.assigned_chores])
        return f"{self.name} (Dostępność: {self.availability}h):\n  {assigned if assigned else 'Nie przydzielono zadan'}"

class HarmonogramZadan: # Klasa z funkcjami odpowiedzialna za zarządzanie zadaniami i członkami rodziny oraz za harmonogram
    def __init__(self):
        self.chores = deque()  # Kolejka zadań do przydzielenia
        self.family_members = []

    def add_chore(self, name, duration):
        self.chores.append(Zadania(name, duration))

    def add_family_member(self, name, availability, preferences=None):
        self.family_members.append(Rodzina(name, availability, preferences))

    def schedule_chores(self): # Funkcja decydująca o tym komu jakie zadanie przydzielić na podstawie preferencji i dostępności
        if not self.family_members:
            print("Brak członkow rodziny do przydzielenia zadan.")
            return

        # Sortowanie członków rodziny po dostępności (ilości wolnych godzin)
        self.family_members.sort(key=lambda member: member.availability, reverse=True)

        while self.chores:
            chore = self.chores.popleft()

            # Preferowane zadania
            preferred_assigned = False
            for member in self.family_members:
                if member.prefers(chore) and member.availability >= chore.duration:
                    member.assign_chore(chore)
                    preferred_assigned = True
                    break

            # Jeśli zadanie nie jest preferowane to przydziel je następnej wolnej osobie
            if not preferred_assigned:
                for member in self.family_members:
                    if member.availability >= chore.duration:
                        member.assign_chore(chore)
                        break
                else:
                    print(f"Nie mozna przydzielic zadania: {chore.name} ({chore.duration}h). Czlonkowie rodziny nie maja czasu.")

    def display_schedule(self): # Funkcja do wyświetlenia harmonogramu
        print("\nHarmonogram zadan:")
        for member in self.family_members:
            print(member)

if __name__ == "__main__":
    scheduler = HarmonogramZadan()

    # Dodawanie członków rodziny z preferencjami
    scheduler.add_family_member("Julia", 5, ["Odkurzanie", "Wyprowadzanie psa"])
    scheduler.add_family_member("Bartek", 4, ["Wyjscie na zakupy"])
    scheduler.add_family_member("Marcin", 6, ["Sprzatanie piwnicy", "Zmywanie naczyn"])
    scheduler.add_family_member("Oliwia", 4, ["Koszenie trawnika"])

    # Dodawanie obowiązków
    scheduler.add_chore("Odkurzanie", 2)
    scheduler.add_chore("Wyjscie na zakupy", 3)
    scheduler.add_chore("Gotowanie obiadu", 2)
    scheduler.add_chore("Zmywanie naczyn", 1)
    scheduler.add_chore("Koszenie trawnika", 4)
    scheduler.add_chore("Wyprowadzeaie psa", 1)
    scheduler.add_chore("Sprzatanie piwnicy", 5)

    # Przydzielenie obowiązków
    scheduler.schedule_chores()

    # Wyświetlenie harmonogramu
    scheduler.display_schedule()
