class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Pracownik(Imie: {self.name}, wiek: {self.age}, wynagrodzenie: {self.salary})"


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f"Pracownik {employee.name} dodany.")

    def display_employees(self):
        if not self.employees:
            print("Brak pracownikow do wyswietlenia.")
        for employee in self.employees:
            print(employee)

    def remove_employees_by_age_range(self, min_age: int, max_age: int):
        initial_count = len(self.employees)
        self.employees = [
            employee for employee in self.employees
            if not (min_age <= employee.age <= max_age)
        ]
        removed_count = initial_count - len(self.employees)
        print(f"{removed_count} usunieto pracownikow w przedziale wiekowym {min_age}-{max_age}.")

    def find_employee_by_name(self, name: str):
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                return employee
        print(f"Pracownik {name} nieznaleziony.")
        return None

    def update_salary_by_name(self, name: str, new_salary: float):
        employee = self.find_employee_by_name(name)
        if employee:
            employee.salary = new_salary
            print(f"Wynagrodzenie pracownika {name} zostalo zaktualizowane do: {new_salary}.")
        else:
            print(f"Pracownik {name} nieznaleziony.")


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def run(self):
        while True:
            print("\nSystem pracownikow - wybierz opcje z listy ponizej:")
            print("1. Dodaj pracownika")
            print("2. Wyswietl pracownikow")
            print("3. Usun pracownikow na podstawie przedzialu wiekowego")
            print("4. Edytuj wynagrodzenie pracownika")
            print("5. Exit")

            choice = input("Wybierz opcje wpisujac liczbe: ")

            if choice == "1":
                name = input("Podaj imie: ")
                age = int(input("Podaj wiek: "))
                salary = float(input("Podaj wynagrodzenie: "))
                employee = Employee(name, age, salary)
                self.manager.add_employee(employee)

            elif choice == "2":
                self.manager.display_employees()

            elif choice == "3":
                min_age = int(input("Podaj minimalny wiek: "))
                max_age = int(input("Podaj maksymalny wiek: "))
                self.manager.remove_employees_by_age_range(min_age, max_age)

            elif choice == "4":
                name = input("Podaj imie pracownika ktoremu chcesz edytowac wynagrodzenie: ")
                new_salary = float(input("Podaj nowe wynagrodzenie: "))
                self.manager.update_salary_by_name(name, new_salary)

            elif choice == "5":
                print("Wychodzisz z systemu pracownika.")
                break

            else:
                print("Nie ma takiej opcji. Sprobouj ponownie.")

if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()
